Testing out implementing Algebraic Data Types in python.
Trying out static type checkers with python.

Setup
=====

For pyenv users, there is a .python-version file.
Then setup a python virtual env.

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    npm install

Run
===

    ./node_modules/.bin/pyright && mypy adt.py && python adt.py

    # This fails with Invalid type annotation 'NoReturn' for x
    # [invalid-annotation] NoReturn is not allowed
    pytype adt.py
    # This one takes awhile; killed after 2 min;
    # maybe because my virtual env folder is inside my project directory?
    # I wonder if it is trying to typecheck all installed python packages.
    pyre
