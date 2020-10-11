from os.path import exists

from setuptools import find_packages, setup

if exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

test_requirements = ['pytest-cov']
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    description="{{ cookiecutter.project_short_description }}",
    keywords='{{ cookiecutter.repo_name }}',
    license="{{ cookiecutter.open_source_license }}",
    classifiers=CLASSIFIERS,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag',
    },
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        "",
    ],
    {% if cookiecutter.include_cli == "y" -%}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:cli'
        ]
    },
    {%- endif %}
    test_suite='{{ cookiecutter.package_name }}/tests',
    tests_require=test_requirements,
    setup_requires=[
        'wheel',
        'setuptools_scm',
        'setuptools>=30.3.0',
        'setuptools_scm_git_archive',
    ],
)
