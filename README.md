# JupyterLab language package template

Jupyterlab language pack template using [copier](https://copier.readthedocs.io).

## Creating a package

To create a package you will need to execute:

```sh
pip install babel copier copier-templates-extensions jinja2-time
mkdir jupyterlab-language-pack
cd jupyterlab-language-pack
copier gh:jupyterlab/language-pack-cookiecutter.git .
```

## Updating a existing package

To update a package you will need to execute in the package folder:

```sh
pip install babel copier copier-templates-extensions jinja2-time
copier update
```
