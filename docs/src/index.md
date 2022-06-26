```@meta
CurrentModule = JuliaPythonAdaptor
```

# JuliaPythonAdaptor

[JuliaPythonAdaptor](https://github.com/thautwarm/JuliaPythonAdaptor.jl) is a small Julia/Python package that helps you to create relocatable applications integrated with Julia and Python together.

The Julia programs using JuliaPythonAdaptor can be compiled by `PackageCompiler` into [sysimages](https://julialang.github.io/PackageCompiler.jl/stable/sysimages.html) or [executables](https://julialang.github.io/PackageCompiler.jl/stable/apps.html) that will work on another machine, if binary-compatible.

## Installation

1. Install a julia (>=1.6.1) distribution. Add it to `$PATH` if you want to avoid manual configurations.

2. Install a Python (3.7+) distribution. Add it to `$PATH` if you want to avoid manual configurations.

3. For the Python distribution: `pip install https://github.com/thautwarm/JuliaPythonAdaptor` or `pip install JuliaPythonAdaptor`

   For the Julia distribution: `julia -e "using Pkg; Pkg.add(\"JSON\", \"JuliaPythonAdaptor\")"`

## Usage

1. (Optionally) Setting up the necessary environment variables for being relocatable.
   The functional environment variables provided by `JuliaPythonAdaptor` is listed in [Configurations](#configurations)

2. If you call Julia from Python, `import JuliaPythonAdaptor` before `import juliacall`.
   
   If you call Python from Julia, `import JuliaPythonAdaptor` before `using PythonCall`.


## Configurations

| Environment Variable  | Description   | Default Value | 
|---|---|---|
| JP_ADAPTOR_PY_EXE  | the Python executable path  | `python` found in `$PATH`  |
| JP_ADAPTOR_JL_EXE  | the Julia executable path  | `julia` found in `$PATH`  |
|  JP_ADAPTOR_JL_PROJ | the Julia project that will be activated  | the global Julia project  |
| JP_ADAPTOR_JL_IMAGE | the Julia Sysimage that will be used | decided by the `julia` program  |
| JP_ADAPTOR_JL_DEPOT_PATH | deciding `JULIA_DEPOT_PATH` | decided by the `julia` program |
