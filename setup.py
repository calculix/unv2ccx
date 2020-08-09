#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

long_description = """Converts Salome .unv file to CalculiX .inp format."""

setuptools.setup(
    name="unv2ccx",
    version="2.0.0",
    author="Ihor Mirzov",
    author_email="imirzov@gmail.com",
    description="Salome to CalculiX converter (unv to inp)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calculix/unv2ccx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)