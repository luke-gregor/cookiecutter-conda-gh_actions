Installation
============

Notes on how to install


##### PyPI
To install the core package run: `pip install {{ cookiecutter.package_name }}`.
Check that you are using the correct version of `pip`.

##### GitHub
For the most up to date version of {{ cookiecutter.project_name }}, you can install directly from the online repository hosted on GitLab.

1. Clone {{ cookiecutter.package_name }} to your local machine: `git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}`
2. Change to the parent directory of {{ cookiecutter.repo_name }}
3. Install glidertools with `pip install -e ./{{ cookiecutter.repo_name }}`. This will allow changes you make locally, to be reflected when you import the package in Python
