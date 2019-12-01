# File setup.py

from setuptools import setup, Extension, find_packages

ctypes_submodule = Extension(
    'ctypes_submodule._ctypes_submodule',
    sources=[
        'ctypes_submodule/add_vectors.c',
    ]
)

setup(
    name='rtd_ctypes_mwe',
    version='0.1',
    url='http://github.com/EricKightley/rtd_ctypes_mwe',
    author='Eric Kightley',
    author_email='kightley.1@gmail.com',
    license='MIT',
    ext_modules = [ctypes_submodule],
    py_modules = ["ctypes_submodule"],
    packages = find_packages(),
    install_requires=[
        'numpy',
        'pytest'
    ],
    zip_safe=False
)
