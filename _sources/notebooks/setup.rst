.. _setup:

Prepare Molecular Density and Grid
##################################

This example on water illustrates all the features related to iterative stockholder analysis (ISA) schemes using `horton-part` package.

The format checkpoint file wavefunction is included in `docs/notebooks/data/co.fchk` and is
read using the [IOData](https://github.com/theochem/iodata) package.

.. literalinclude:: setup.py
    :language: python
    :lines: 1-34

Some helper functions are also defined in `setup.py` file.

.. literalinclude:: setup.py
    :language: python
    :lines: 37-
