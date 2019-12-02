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

Documentation
-------------

Documentation is built using sphinx in the ``docs`` directory. Details of
the build process are as follows:

- Initialization via ``sphinx-quickstart``.
- Creation of ``ctypes_submodule.rst``.
- Modification of ``index.rst`` to include ``ctypes_submodule``.
- Uncommenting lines 13-15 of ``conf.py`` and modifying the path on line
  15 from ``.`` to ``..`` so that the documentation can be found locally.
- Adding ``'sphinx.ext.autodoc'`` the list of extensions in
- Adding ``master_doc = 'index'`` to ``conf.py`` so that readthedocs knows to replace
  ``contents.rst`` with ``index.rst``.


To verify that the documentation builds correctly locally,
after installing the package as above, in the ``docs`` directory run:

    make html

Then ``_build/html/ctypes_submodule.html`` has auto-generated documentation for
the ``add_vectors`` function.
