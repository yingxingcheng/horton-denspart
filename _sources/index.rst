.. image:: horton_part_logo.svg
  :width: 450
  :align: center


Welcome to Horton-Part's documentation!
=======================================

`HORTON-PART <https://github.com/yingxingcheng/horton-part>`_ is a computational chemistry package that supports different partition schemes.
It is based on the sub-module ``part`` of ``HORTON2``, which is written and maintained by Toon Verstraelen (2).
In ``HORTON3``, all sub-modules have been rewritten using the pure Python programming language to support Python 3+.
See more details on this `website <http://theochem.github.com/horton/>`_.
It should be noted that ``HORTON2`` also supports Python 3+ now.
The ``part`` module has also been rewritten and is now called `denspart <https://github.com/theochem/denspart>`_ module.
However, the algorithm implemented in ``denspart`` only uses one-step optimization, which can be computationally expensive for large systems.
Additionally, ``denspart`` only supports the ``MBIS`` partitioning scheme.
Another ``part`` module has been rewritten in pure Python programming language by Farnaz Heidar-Zadeh (2).
However, the integration grid implemented in this module still uses the old 'grid' from Horton2.
`HORTON-PART <https://github.com/yingxingcheng/horton-part>`_ with version ``0.0.X`` is based on this module.
Starting from version ``1.X.X``, `HORTON-PART <https://github.com/yingxingcheng/horton-part>`_ only supports the new integration `qc-grid <https://github.com/theochem/grid>`_.
The molecular density can be prepared using ``IOData`` (https://github.com/theochem/iodata) and ``GBasis`` (https://github.com/theochem/gbasis) packages.

This version contains contributions from
YingXing Cheng (1),
Toon Verstraelen (2),
Pawel Tecmer (3),
Farnaz Heidar-Zadeh (3),
Cristina E. González-Espinoza (3),
Matthew Chan (3),
Taewon D. Kim (3),
Katharina Boguslawski (3),
Stijn Fias (4),
Steven Vandenbrande (2),
Diego Berrocal (3),
and Paul W. Ayers (3)

- (1) Numerical Mathematics for High Performance Computing (NMH), University of Stuttgart, Stuttgart, Germany.
- (2) Center for Molecular Modeling (CMM), Ghent University, Ghent, Belgium.
- (3) The Ayers Group, McMaster University, Hamilton, Ontario, Canada.
- (4) General Chemistry (ALGC), Free University of Brussels, Brussels, Belgium.

The ``Horton-Part`` source code is hosted on GitHub and is released under the GNU General Public License v3.0.
Please report any issues you encounter while using ``Horton-Part`` library on
`GitHub Issues <https://github.com/yingxingcheng/horton-part/issues/new>`_.
For further information and inquiries please contact us at yxcheng2buaa@gmail.com.


Functionality
=============
* Real space partitioning schemes

  * Mulliken partitioning method

* Density related partitioning schemes

  * Becke partitioning method

  * Stockholder schemes

    * Hirshfeld partitioning method

  * Iterative Stockholder schemes

    * Iterative Hirshfeld (Hirshfeld-I) partitioning method

    * Iterative Stockholder Approach (ISA)

    * Minimal Basis Iterative Stockholder (MBIS)

    * Gaussian iterative stockholder approach (GISA)

    * Alternating Linear approximation of the ISA (aLISA) method

    * Global Linear approximation of the ISA (gLISA) method

    * Generalized Minimal Basis Iterative Stockholder (GMBIS)

    * Non-linear approximation of the ISA (NLIS) method


Citations
=========

Please use the following citations in any publication using ``horton-part`` library:

[1] Cheng, Y.; Cancès, E.; Ehrlacher, V.; Misquitta, A. J.; Stamm, B.
**Multi-center decomposition of molecular densities: A numerical perspective.**
`arXiv 2024, 2405.08455 <https://doi.org/10.48550/arXiv.2405.08455>`_

[2] Benda, R.; Cancès, E.; Ehrlacher, V.; Stamm, B.
**Multi-center decomposition of molecular densities: A mathematical perspective.**
`J. Chem. Phys. 2022, 156, 164107 <https://doi.org/10.1063/5.0076630>`_

[3] Chan, M.; Verstraelen, T.; Tehrani, A.; Richer, M.; Yang, X. D.; Kim, T. D.; Vöhringer-Martinez, E.; Heidar-Zadeh, F.; Ayers, P. W.
**The tale of HORTON: Lessons learned in a decade of scientific software development.**
`J. Chem. Phys. 2024, 160, 162501 <https://doi.org/10.1063/5.0196638>`_

[4] Tehrani, A.; Yang, X. D.; Martínez-González, M.; Pujal, L.; Hernández-Esparza, R.; Chan, M.; Vöhringer-Martinez, E.; Verstraelen, T.; Ayers, P. W.; Heidar-Zadeh, F.
**Grid: A Python library for molecular integration, interpolation, differentiation, and more.**
`J. Chem. Phys. 2024, 160, 172503 <https://doi.org/10.1063/5.0202240>`_

[5] Kim, T. D.; Pujal, L.; Richer, M.; van Zyl, M.; Martínez-González, M.; Tehrani, A.; Chuiko, V.; Sánchez-Díaz, G.; Sanchez, W.; Adams, W.; Huang, X.; Kelly, B. D.; Vöhringer-Martinez, E.; Verstraelen, T.; Heidar-Zadeh, F.; Ayers, P. W.
**GBasis: A Python library for evaluating functions, functionals, and integrals expressed with Gaussian basis functions.**
`J. Chem. Phys. 2024, 161, 042503 <https://doi.org/10.1063/5.0216776>`_

[6] Verstraelen, T.; Adams, W.; Pujal, L.; Tehrani, A.; Kelly, B. D.; Macaya, L.; Meng, F.; Richer, M.; Hernández-Esparza, R.; Yang, X. D.; Chan, M.; Kim, T. D.; Cools-Ceuppens, M.; Chuiko, V.; Vöhringer-Martinez, E.; Ayers, P. W.; Heidar-Zadeh, F.
**IOData: A python library for reading, writing, and converting computational chemistry file formats and generating input files.**
`J. Comput. Chem. 2021, 42, 458–464 <https://doi.org/10.1002/jcc.26468>`_


Modules
=======

.. csv-table::
    :file: ./table_modules.csv
    :widths: 50, 70
    :delim: ;
    :header-rows: 1
    :align: center


.. toctree::
    :maxdepth: 2
    :caption: User Documentation

    ./installation.rst



.. toctree::
    :maxdepth: 1
    :caption: Quick Start

    ./notebooks/quick_start.ipynb


.. toctree::
    :maxdepth: 1
    :caption: Example Tutorials

    ./notebooks/setup.rst
    ./notebooks/isa.ipynb
    ./notebooks/gisa.ipynb
    ./notebooks/mbis.ipynb
    ./notebooks/lisa.ipynb
    ./notebooks/lisa_diis.ipynb
    ./notebooks/glisa.ipynb

    ./notebooks/hirshfeld.ipynb
    ./notebooks/mulliken.ipynb


.. toctree::
   :maxdepth: 2
   :caption: API Documentation

   pyapi/modules.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
