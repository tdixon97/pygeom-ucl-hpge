# pygeom-ucl-hpge

A package for implementing the geometry of the UCL HPGe detector in
`pyg4ometry`.

## Installation

First clone the repository.

```console 
git clone https://github.com/tdixon97/pygeom-ucl-hpge
```

Then the package can be installed with pip.

```console
    pip install -e .
```

Or:

```console
    pip install -e .[test]
```
We follow the best practices defined in [pygama-developers-guide](https://pygama.readthedocs.io/en/stable/developer.html)

For example a series of  pre-commit hooks are employed (similar to pygama) to check the code. Before making any pull request you should run:

```console 

    pre-commit run --all-files

```
