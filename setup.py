#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['tqdm==4.32.2', 'sparqlwrapper==1.8.2', 'pandas==0.24.1']

setup_requirements = []

test_requirements = []

setup(
    author="Armand Boschin",
    author_email='aboschin@enst.fr',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="Break WikiData dumps into smaller knowledge graphs",
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords='wikidatasets',
    name='wikidatasets',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/armand33/wikidatasets',
    version='0.2.1',
    zip_safe=False,
)
