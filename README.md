# cookiecutter-conda-gh_actions
A [cookiecutter](https://www.github.com/audreyr/cookiecutter "cookiecutter") template for Python projects using conda and GitHub actions for testing and deployment

## Features

 - Makefile with commands to set up the environment, test, lint and deploy documentation as a GitHub page
 - Pre-configured for GitHub actions for 
   - testing: can run multiple OS and python versions
   - deployment to PyPi: currently builds on 3.7 in ubuntu
 - Automatic versioning and deployment (requires git annotated tags before it'll work). Can be integrated with Zenodo for automatic DOI generation
 - setup.cfg with black, flake8 opinions and pytest/pytest-cov configuration
 - basic setup will have a command line interface (CLI)

## Installation

This cookiecutter assumes that you have git and a version of conda installed.

Prior to installing cookiecutter-conda-python, the cookiecutter package must be installed in your environment. This is achieved via the following command::

    $ conda install cookiecutter

With cookiecutter installed, the cookiecutter-conda-python template can be installed with::

    $ cookiecutter https://github.com/luke-gregor/cookiecutter-conda-gh_actions.git

Once cookiecutter clones the template, you will be asked a series of questions related to your project::

    $ full_name [Full Name]: Enter your full name.

    $ email [Email Address]: Enter your email address.

    $ github_username [github_username]: Enter your github username.

    $ repo_name [repository_name]: Enter the name of your project's repository.

    $ package_name [package_name]: Enter the name of your package.

    $ application_name [application]: Enter the name of your GUI application.

    $ project_short_description [Short description]: Enter a short description about your project.


## Usage

After answering the questions asked during installation, a conda Python package will be
created in your current working directory. This package will contain a simple CLI script
and the conda recipe necessary to build the application into a conda package.

You can also type `make` in the temrinal to see a list of commands. 
I recommend that you run `make dev_environment` to set up the conda environment.

Documentation can be built with `mkdocs build` or served live with `mkdocs serve`. 
Running `mkdocs gh-deploy` will create a GitHub pages site. 

You need to enter your PyPi password under the repository settings, secrets as `PYPI_PASSWORD`
