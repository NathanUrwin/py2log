#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pylog setuptools module.
"""

from setuptools import setup, find_packages

setup(
    name="py2log",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
