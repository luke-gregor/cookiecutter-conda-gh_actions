=====================
Contribution Guide
=====================

Contributions are highly welcomed and appreciated.  Every little help counts,
so do not hesitate! You can make a high impact on ``{{ cookiecutter.repo_name }}`` just by using it and
reporting `issues <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues>`__.

The following sections cover some general guidelines
regarding development in ``{{ cookiecutter.repo_name }}`` for maintainers and contributors.

Please also review our `Code of Conduct <code_of_conduct.html>`__.

Nothing here is set in stone and can't be changed.
Feel free to suggest improvements or changes in the workflow.



.. contents:: Contribution links
   :depth: 2



.. _submitfeedback:

Feature requests and feedback
-----------------------------

We are eager to hear about your requests for new features and any suggestions about the
API, infrastructure, and so on. Feel free to submit these as
`issues <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues/new>`__ with the label "feature request."

Please make sure to explain in detail how the feature should work and keep the scope as
narrow as possible. This will make it easier to implement in small PRs.


.. _reportbugs:

Report bugs
-----------

Report bugs for ``{{ cookiecutter.repo_name }}`` in the `issue tracker <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues>`_
with the label "bug".

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting,
  specifically the Python interpreter version, installed libraries, and ``{{ cookiecutter.repo_name }}``
  version.
* Detailed steps to reproduce the bug.

If you can write a demonstration test that currently fails but should passm
that is a very useful commit to make as well, even if you cannot fix the bug itself.


.. _fixbugs:

Fix bugs
--------

Look through the `GitHub issues for bugs <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/labels/bug>`_.

Talk to developers to find out how you can fix specific bugs.



Preparing Pull Requests
-----------------------


#. Fork the
   `{{ cookiecutter.repo_name }} GitHub repository <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}>`__.  It's
   fine to use ``{{ cookiecutter.repo_name }}`` as your fork repository name because it will live
   under your user.

#. Clone your fork locally using `git <https://git-scm.com/>`_, connect your repository
   to the upstream (main project), and create a branch::

    $ git clone git@github.com:YOUR_GITHUB_USERNAME/{{ cookiecutter.repo_name }}.git
    $ cd {{ cookiecutter.repo_name }}
    $ git remote add upstream git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

    # now, to fix a bug or add feature create your own branch off "master":

    $ git checkout -b your-bugfix-feature-branch-name master

   If you need some help with Git, follow this quick start
   guide: https://git.wiki.kernel.org/index.php/QuickStart

#. Install dependencies into a new conda environment::

    $ conda env update -f ci/environment-dev-3.6.yml
    $ conda activate {{ cookiecutter.repo_name }}-dev

#. Make an editable install of {{ cookiecutter.repo_name }} by running::

    $ pip install -e .

#. Install `pre-commit <https://pre-commit.com>`_ and its hook on the ``{{ cookiecutter.repo_name }}`` repo::

     $ pip install --user pre-commit
     $ pre-commit install

   Afterwards ``pre-commit`` will run whenever you commit.

   https://pre-commit.com/ is a framework for managing and maintaining multi-language pre-commit
   hooks to ensure code-style and code formatting is consistent.

    Now you have an environment called ``{{ cookiecutter.repo_name }}-dev`` that you can work in.
    You’ll need to make sure to activate that environment next time you want
    to use it after closing the terminal or your system.

    You can now edit your local working copy and run/add tests as necessary. Please follow
    PEP-8 for naming. When committing, ``pre-commit`` will modify the files as needed, or
    will generally be quite clear about what you need to do to pass the commit test.

#. Break your edits up into reasonably sized commits::

    $ git commit -a -m "<commit message>"
    $ git push -u

#. Run all the tests

   Now running tests is as simple as issuing this command::

    $ pytest {{ cookiecutter.repo_name }}

   Check that your contribution is covered by tests and therefore increases the overall test coverage::

    $ coverage run --source {{ cookiecutter.repo_name }} -m py.test
    $ coverage report
    $ coveralls

  Please stick to `xarray <http://xarray.pydata.org/en/stable/contributing.html>`_'s testing recommendations.


#. Create a new changelog entry in ``CHANGELOG.rst``:

   - The entry should be entered as:

    <description> (``:pr:`#<pull request number>```) ```<author's names>`_``

    where ``<description>`` is the description of the PR related to the change and
    ``<pull request number>`` is the pull request number and ``<author's names>`` are your first
    and last names.

   - Add yourself to list of authors at the end of ``CHANGELOG.rst`` file if not there yet, in
     alphabetical order.

 #. Add yourself to the
    `contributors <https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/contributors.html>`_
    list via ``docs/source/contributors.rst``.

#. Finally, submit a pull request through the GitHub website using this data::

    head-fork: YOUR_GITHUB_USERNAME/{{ cookiecutter.repo_name }}
    compare: your-branch-name

    base-fork: {{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
    base: master

Note that you can create the Pull Request while you're working on this. The PR will update
as you add more commits. ``{{ cookiecutter.repo_name }}`` developers and contributors can then review your code
and offer suggestions.
