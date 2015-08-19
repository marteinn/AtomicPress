#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pip

from setuptools import setup, find_packages
from pip.req import parse_requirements
import atomicpress

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


packages = find_packages()

# Handle requirements
requires = parse_requirements("requirements/install.txt",
                              session=pip.download.PipSession())
install_requires = [str(ir.req) for ir in requires]

requires = parse_requirements("requirements/tests.txt",
                              session=pip.download.PipSession())
tests_require = [str(ir.req) for ir in requires]

# Convert markdown to rst
try:
    from pypandoc import convert
    long_description = convert("README.md", "rst")
except ImportError:
    long_description = open("README.md").read()

setup(
    name="atomicpress",
    version=atomicpress.__version__,
    description=("AtomicPress is a static blog generator for python developers."),  # NOQA
    long_description=long_description,
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/atomicpress",
    packages=packages,
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 2.7"
    ),
)
