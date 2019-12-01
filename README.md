# rtd_ctypes_mwe
Minimum working example to generate documentation on readthedocs.io for a
python package with a ctypes shared library.

Installation
------------

To install the package, clone the repository, make a virtual environment and
activate it, change directory to `rdt_ctypes_mwe/`, then:

    python setup.py build_ext --inplace
    pip install .

To test the installation, run:

    pytest
