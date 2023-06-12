# -*- coding: utf-8 -*-
import os
from setuptools import setup

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
accepted_filetypes = (".html", ".png", ".svg", ".js", ".css")

for dirpath, dirnames, filenames in os.walk("ab_plugin_plugin_name"):
    # Ignore dirnames that start with '.'
    if ('__init__.py' in filenames
            or any(x.endswith(accepted_filetypes) for x in filenames)):
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)

if 'VERSION' in os.environ:
    version = os.environ['VERSION']
else:
    version = os.environ.get('GIT_DESCRIBE_TAG', '0.0.0')

setup(
    name="ab-plugin-plugin_name",
    version=version,
    packages=packages,
    include_package_data=True,
    author="plugin_author",
    author_email="plugin_author_email",
    license=open('LICENSE.txt').read(),
    install_requires=[], # dependency management in conda recipe
    url="plugin_url",
    long_description=open('README.md').read(),
    description="one_line_description",
    )
