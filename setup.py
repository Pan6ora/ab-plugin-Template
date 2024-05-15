# -*- coding: utf-8 -*-
import os
from setuptools import setup

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk("ab_online"):
    # Ignore dirnames that start with '.'
    if "__init__.py" in filenames or "includes" in dirpath:
        pkg = dirpath.replace(os.path.sep, ".")
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, ".")
        packages.append(pkg)

if 'VERSION' in os.environ:
    version = os.environ['VERSION']
else:
    version = os.environ.get('GIT_DESCRIBE_TAG', '0.0.0')

setup(
    name="ab-plugin-template",
    version=version,
    packages=packages,
    include_package_data=True,
    author="Rémy Le Calloch",
    author_email="remy@lecalloch.net",
    license=open('LICENSE.txt').read(),
    install_requires=[],  # dependency management in conda recipe
    url="https://github.com/Pan6ora/activity-browser-plugin-template",
    long_description=open('README.md').read(),
    description="An empty plugin to start from",
)
