# -*- coding: utf-8 -*-
import codecs
from setuptools import setup, find_packages
extra_setup = dict(
install_requires=[
    'wheel',
],
)

setup(
    name='sphinx-docfx-markdown',
    version='1.2.43',
    author='Xavier Dupré',
    author_email='xaduprec@microsoft.com',
    url='https://github.com/xadupre/sphinx-docfx-markdown',
    description='Sphinx Python Domain to DocFX Markdown Generator',
    requires=open("requirements.txt", "r").readlines(),
    package_dir={'': '.'},
    packages=find_packages('.', exclude=['tests']),
    long_description=codecs.open("README.rst", "r", "utf-8").read(),
    # trying to add files...
    include_package_data=True,
    **extra_setup
)
