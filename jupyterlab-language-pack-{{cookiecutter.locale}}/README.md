{%- set loc = cookiecutter.locale.replace("_", "-") -%}
# Jupyterlab {{ cookiecutter.language }} Language Pack

{{ cookiecutter.language }} language pack for the JupyterLab ecosystem.

## Install

### pip

```bash
pip install jupyterlab-language-pack-{{ loc }}
```

### conda

```bash
conda install jupyterlab-language-pack-{{ loc }} -c conda-forge
```

## Contributing

To contribute to this package please visit the [Crowdin site](https://crowdin.com/project/jupyterlab).
