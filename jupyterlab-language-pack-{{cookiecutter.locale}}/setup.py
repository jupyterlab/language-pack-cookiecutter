from setuptools import find_packages, setup

setup(
    name="jupyterlab_language_pack_{{ cookiecutter.locale }}",
    version='0.1.0',
    url='https://github.com/goanpeca/jupyterlab-language-packs',
    description='Jupyterlab {{ cookiecutter.language }} Language Pack',
    install_requires=["jupyterlab_language==0.1.0"],
    packages=find_packages(),
    entry_points={'jupyterlab.languagepacks': '{{ cookiecutter.locale }} = jupyterlab_language_pack_{{ cookiecutter.locale }}'},
)
