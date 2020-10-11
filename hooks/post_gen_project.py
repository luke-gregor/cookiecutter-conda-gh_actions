#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_comments(filepath):
    import re
    filepath = os.path.join(PROJECT_DIRECTORY, filepath)
    string = open(filepath, 'r').read()
    string = re.sub("\n# ", "\n", string)

    with open(filepath + '.tmp', 'w') as file:
        file.write(string)

    os.remove(filepath)
    os.rename(filepath + '.tmp', filepath)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.open_source_license }}' == 'Proprietary':
        remove_file('LICENSE')

    if '{{ cookiecutter.include_cli }}' != 'y':
        remove_file('{{ cookiecutter.package_name }}/__main__.py')
        remove_file('{{ cookiecutter.package_name }}/cli.py')
        remove_file('tests/test_cli.py')

    remove_comments('.pre-commit-config.yaml')
