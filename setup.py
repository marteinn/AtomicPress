#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages
from pip.req import parse_requirements
import atomicpress

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


packages = find_packages()

with open('README.md') as f:
    readme = f.read()

requires = parse_requirements("requirements.txt")
install_requires = [str(ir.req) for ir in requires]


long_description = """
AtomicPress is a static blog generator for python developers that don't want
the WordPress security hassle.

---

%s

""" % readme


setup(
    name="atomicpress",
    version=atomicpress.__version__,
    description=("AtomicPress is a static blog generator for python developers "
                 "that don't want the WordPress security hassle."),
    long_description=long_description,
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/atomicpress",
    packages=packages,
    include_package_data=True,
    install_requires=install_requires,
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