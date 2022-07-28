# -*- coding: utf-8 -*-
import os
from setuptools import setup

from .metadata import *

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
accepted_filetypes = (".html", ".png", ".svg", ".js", ".css")

for dirpath, dirnames, filenames in os.walk('plugin'):
    # Ignore dirnames that start with '.'
    if ('__init__.py' in filenames
            or any(x.endswith(accepted_filetypes) for x in filenames)):
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)

setup(
    name=name,
    version=version,
    packages=packages,
    include_package_data=True,
    author=author,
    author_email=author_email,
    license=open('LICENSE.txt').read(),
    install_requires=[], # dependency management in conda recipe
    url=url,
    long_description=open('README.md').read(),
    description=description,
    classifiers=classifiers,
    )
