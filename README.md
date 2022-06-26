# JuliaPythonAdaptor

[JuliaPythonAdaptor](https://github.com/thautwarm/JuliaPythonAdaptor.jl) is a small Julia/Python package that helps you to create relocatable applications integrated with Julia and Python together.

The Julia programs using JuliaPythonAdaptor can be compiled by `PackageCompiler` into [sysimages](https://julialang.github.io/PackageCompiler.jl/stable/sysimages.html) or [executables](https://julialang.github.io/PackageCompiler.jl/stable/apps.html) that will work on another machine, if binary-compatible.

Note that your Python binaries are NOT bundled in the compiled julia files. You should also provide a property Python environment for the target machines.

## Motivation

At the current stage, a Julia programmer suffers from the following tasks:

1. Setting up a Python environment to work with Julia.

2. Reusing an existing Python/Julia environment from another language.

3. Distributing compiled Julia binaries that interoperate with Python packages.

This project aims at providing a user-friendly approach to address all above issues.

## Target Uses

1. Software Integration

    If you want to make software that bundle Julia and Python together and make a separated environment, you might consider using this package or refer to the implementation.

2. Simple Python-Julia Interoperability

    If your activating environment contains `julia` and `python`, you you don't need to consider details.

## Installation

1. Install a julia (>= 1.6.1) distribution. Add it to `$PATH` if you want to avoid manual configurations.

2. Install a Python (3.7+) distribution. Add it to `$PATH` if you want to avoid manual configurations.

3. For the Python distribution: `pip install https://github.com/thautwarm/JuliaPythonAdaptor` or `pip install JuliaPythonAdaptor`

   For the Julia distribution: `julia -e "using Pkg; Pkg.add(\"JSON\", \"JuliaPythonAdaptor\")"`

## Usage

For relocatability, you might add the following environment variables:

| Environment Variable  | Description   | Default Value | 
|---|---|---|
| JP_ADAPTOR_PY_EXE  | the Python executable path  | `python` found in `$PATH`  |
| JP_ADAPTOR_JL_EXE  | the Julia executable path  | `julia` found in `$PATH`  |
|  JP_ADAPTOR_JL_PROJ | the Julia project that will be activated  | the global Julia project  |
| JP_ADAPTOR_JL_IMAGE | the Julia Sysimage that will be used | decided by the `julia` program  |
| JP_ADAPTOR_JL_DEPOT_PATH | deciding `JULIA_DEPOT_PATH` | decided by the `julia` program |


Then, if you call Python from Julia, `import JuliaPythonAdaptor` before you import `PythonCall`. If you call Julia from Python, `import JuliaPythonAdaptor` before you import `juliacall`.


## I use PyCall, how to use this package?

PyCall is a great package for Julia to call Python, but it so far does not consider much about relocatability and environment separation.

Please refer to these detailed instructions [from PyCall to PythonCall](https://cjdoris.github.io/PythonCall.jl/stable/pycall/). They will help you with migrating your codebase.

## Contributions

PRs and issues are welcome.

Besides, this project leverages the mechanism provided by [PythonCall.jl](https://github.com/cjdoris/PythonCall.jl), [CondaPkg.jl](https://github.com/cjdoris/CondaPkg.jl/), [MicroMamba.jl](https://github.com/cjdoris/MicroMamba.jl) and [pyjuliapkg](https://github.com/cjdoris/pyjuliapkg). You might also consider contributing to them.
