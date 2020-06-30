# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
 
from setuptools import setup
{% set loc = cookiecutter.locale %}

setup(
    name="jupyterlab_language_pack_{{loc}}",
    version="0.1.0",
    url="https://github.com/goanpeca/jupyterlab-language-packs",
    description="Jupyterlab {{ cookiecutter.language }} Language Pack",
    install_requires=[],
    packages=[
        "jupyterlab_language_pack_{{loc}}",
        "jupyterlab_language_pack_{{loc}}.extensions",
    ],
    package_dir={
        "jupyterlab_language_pack_{{loc}}": "jupyterlab_language_pack_{{loc}}",
        "jupyterlab_language_pack_{{loc}}.extensions": "jupyterlab_language_pack_{{loc}}/extensions",
    },
    package_data={
        "jupyterlab_language_pack_{{loc}}": ["*.json", "*.mo"],
        "jupyterlab_language_pack_{{loc}}.extensions": ["*.json", "*.mo",],
    },
    entry_points={
        "jupyterlab.languagepack": ["{{loc}} = jupyterlab_language_pack_{{loc}}",]
    },
)
