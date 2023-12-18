import argparse
import sys
import numpy as np
from grid.molgrid import MolGrid
from grid.basegrid import OneDGrid
from grid.atomgrid import AtomGrid
from horton_part import wpart_schemes
import logging

width = 100
np.set_printoptions(precision=14, suppress=True, linewidth=np.inf)
np.random.seed(44)

__all__ = ["construct_molgrid_from_dict"]


logger = logging.getLogger(__name__)


def construct_molgrid_from_dict(data):
    atcoords = data["atcoords"]
    atnums = data["atnums"]
    # atcorenums = data["atcorenums"]
    aim_weights = data["aim_weights"]
    natom = len(atnums)

    # build atomic grids
    atgrids = []
    for iatom in range(natom):
        rgrid = OneDGrid(
            points=data[f"atom{iatom}/rgrid/points"],
            weights=data[f"atom{iatom}/rgrid/weights"],
        )
        shell_idxs = data[f"atom{iatom}/shell_idxs"]
        sizes = shell_idxs[1:] - shell_idxs[:-1]
        # center = atcoords[iatom]
        atgrid = AtomGrid(rgrid, sizes=sizes, center=atcoords[iatom], rotate=0)
        atgrids.append(atgrid)

    return MolGrid(atnums, atgrids, aim_weights=aim_weights, store=True)


def main():
    """Main program."""
    args = parse_args()
    # Convert the log level string to a logging level
    log_level = getattr(logging, args.log.upper(), None)
    if not isinstance(log_level, int):
        raise ValueError(f"Invalid log level: {args.log}")

    if log_level > logging.DEBUG:
        logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")
    else:
        logging.basicConfig(level=log_level)

    logger.info("*" * width)
    logger.info(f"Reade grid and density data from {args.filename}")
    logger.info("*" * width)
    data = np.load(args.filename)
    grid = construct_molgrid_from_dict(data)

    logger.info(" " * width)
    logger.info("*" * width)
    logger.info(" Partitioning ".center(width, " "))
    logger.info("*" * width)
    kwargs = {
        "coordinates": data["atcoords"],
        "numbers": data["atnums"],
        "pseudo_numbers": data["atcorenums"],
        "grid": grid,
        "moldens": data["density"],
        "lmax": args.lmax,
        "maxiter": args.maxiter,
        "threshold": args.threshold,
        "local_grid_radius": args.local_grid_radius,
    }

    if args.type in ["gisa", "lisa"]:
        kwargs["solver"] = args.solver
        if args.type in ["lisa"]:
            kwargs["basis_func_type"] = args.func_type
            kwargs["basis_func_json_file"] = args.func_file
            kwargs["use_global_method"] = args.use_global_method
            if args.solver > 200:
                kwargs["diis_size"] = args.diis_size

    part = wpart_schemes(args.type)(**kwargs)
    part.do_partitioning()
    # part.do_moments()

    logger.info(" " * width)
    logger.info("*" * width)
    logger.info(" Results ".center(width, " "))
    logger.info("*" * width)
    logger.info("charges:")
    logger.info(part.cache["charges"])
    # logger.info("cartesian multipoles:")
    # logger.info(part.cache["cartesian_multipoles"])
    # logger.info("radial moments:")
    # logger.info(part.cache["radial_moments"])

    if not (args.type in ["lisa"] and args.use_global_method):
        logger.info(" " * width)
        logger.info("*" * width)
        logger.info(" Time usage ".center(width, " "))
        logger.info("*" * width)
        logger.info(
            f"Do Partitioning                              : {part.time_usage['do_partitioning']:>10.2f} s"
        )
        logger.info(
            f"  Update Weights                             : {part._cache['time_update_at_weights']:>10.2f} s"
        )
        logger.info(
            f"    Update Promolecule Density (N_atom**2)   : {part._cache['time_update_promolecule']:>10.2f} s"
        )
        logger.info(
            f"    Update AIM Weights (N_atom)              : {part._cache['time_compute_at_weights']:>10.2f} s"
        )
        logger.info(
            f"  Update Atomic Parameters (iter*N_atom)     : {part._cache['time_update_propars_atoms']:>10.2f} s"
        )
        # logger.info(f"Do Moments                                   : {part.time_usage['do_moments']:>10.2f} s")
        logger.info("*" * width)
        logger.info(" " * width)

    part_data = {}
    part_data["natom"] = len(data["atnums"])
    part_data["atnums"] = data["atnums"]
    part_data["atcorenums"] = data["atcorenums"]
    part_data["type"] = args.type
    part_data["lmax"] = args.lmax
    part_data["maxiter"] = args.maxiter
    part_data["threshold"] = args.threshold
    part_data["solver"] = args.solver
    part_data["charges"] = part.cache["charges"]

    if not (args.type in ["lisa"] and args.use_global_method):
        part_data["time"] = part.time_usage["do_partitioning"]
        part_data["time_update_at_weights"] = part._cache["time_update_at_weights"]
        part_data["time_update_promolecule"] = part._cache["time_update_promolecule"]
        part_data["time_compute_at_weights"] = part._cache["time_compute_at_weights"]
        part_data["time_update_propars_atoms"] = part._cache[
            "time_update_propars_atoms"
        ]
        part_data["niter"] = part.cache["niter"]
        part_data["history_charges"] = part.cache["history_charges"]
        part_data["history_propars"] = part.cache["history_propars"]
        part_data["history_entropies"] = part.cache["history_entropies"]

    # part_data["part/cartesian_multipoles"] = part.cache["cartesian_multipoles"]
    # part_data["part/radial_moments"] = part.cache["radial_moments"]
    part_data.update(data)
    np.savez_compressed(args.output, **part_data)


def parse_args():
    """Parse command-line arguments."""
    description = "Molecular density partitioning with HORTON3."
    parser = argparse.ArgumentParser(prog="part-dens", description=description)

    # for part
    parser.add_argument(
        "filename",
        type=str,
        help="The output file of part-gen command.",
    )
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        default="lisa",
        choices=["gisa", "lisa", "mbis", "is"],
        help="Number of angular grid points. [default=%(default)s]",
    )
    parser.add_argument(
        "--func_type",
        type=str,
        default="gauss",
        choices=["gauss", "slater"],
        help="The type of basis functions. [default=%(default)s]",
    )
    parser.add_argument(
        "--func_file",
        type=str,
        default=None,
        help="The json filename of basis functions.",
    )
    parser.add_argument(
        "--maxiter",
        type=int,
        default=1000,
        help="The maximum iterations. [default=%(default)s]",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=1e-6,
        help="The threshold of convergence. [default=%(default)s]",
    )
    parser.add_argument(
        "--lmax",
        type=int,
        default=3,
        help="The maximum angular momentum in multipole expansions. [default=%(default)s]",
    )
    parser.add_argument(
        "--solver",
        type=int,
        default=2,
        help="The objective function type for GISA and LISA methods. [default=%(default)s]",
    )
    parser.add_argument(
        "--diis_size",
        type=int,
        default=8,
        help="The number of previous iterations info used in DIIS. [default=%(default)s]",
    )
    parser.add_argument(
        "--use_global_method",
        default=False,
        action="store_true",
        help="Whether use global method",
    )
    parser.add_argument(
        "--local_grid_radius",
        type=float,
        default=np.inf,
        help="The radius for local atomic grid [default=%(default)s]",
    )
    parser.add_argument(
        "--output",
        help="The NPZ file in which the partitioning results will be stored.",
        type=str,
        default="partitioning.npz",
    )
    # parser.add_argument(
    #     "--verbose",
    #     type=int,
    #     default=3,
    #     help="The level for printing output information. [default=%(default)s]",
    # )
    parser.add_argument(
        "--log",
        default="INFO",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: %(default)s)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())
