#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="pyopenfec",
      version="0.2.0",
      description="OpenFEC API client",
      license="MIT",
      install_requires=["requests", "six"],
      author="Jeremy Bowers",
      author_email="jeremyjbowers@gmail.com",
      url="http://github.com/jeremyjbowers/pyopenfec",
      packages=find_packages(),
      keywords="fec campaign finance openfec",
      classifiers=['Development Status :: 4 - Beta'],
      zip_safe=True)
