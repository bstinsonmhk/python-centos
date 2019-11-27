#!/usr/bin/python

from setuptools import find_packages, setup

setup(
    name="centos",
    description="Client-side modules for CentOS Services",
    author="Brian Stinson",
    author_email="brian@bstinson.com",
    packages=find_packages(),
    license='GPLv2',
    version='0.1.1',
    install_requires=[
        "kitchen",
        "lockfile",
        "munch",
        "pyOpenSSL",
        "requests",
        "urllib3",
    ],
)
