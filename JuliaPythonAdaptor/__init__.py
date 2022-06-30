import ctypes
import os
import sys

jl_info = r"""
import Pkg
import JSON
println(
    JSON.json(
        Dict{String, String}(
            "depot_path" => DEPOT_PATH[1],
            "julia_exe" => Base.julia_cmd().exec[1],
            "sysimage" => unsafe_string(Base.JLOptions().image_file),
            "project" => dirname(Pkg.project().path)
        )
    )
)
"""

def env_descriptor(varname):
    @property
    def get(self):
        if self._env is None:
            env = os.environ
        else:
            env = self._env
        return env.get(varname, '')

    @get.setter
    def set(self, value):
        if self._env is None:
            env = os.environ
        else:
            env = self._env
        env[varname] = value

    return set

class ENV:
    JP_ADAPTOR_PY_EXE: str
    JP_ADAPTOR_CONDA_EXE: str
    JP_ADAPTOR_JL_EXE: str
    JP_ADAPTOR_JL_PROJ: str
    JP_ADAPTOR_JL_IMAGE: str
    JP_ADAPTOR_JL_DEPOT_PATH: str

    JP_ADAPTOR_INITIALIZED: str

    PYTHON_JULIAPKG_OFFLINE: str
    PYTHON_JULIAPKG_PROJECT: str
    PYTHON_JULIAPKG_EXE: str

    JULIA_PYTHONCALL_PROJECT: str
    JULIA_PYTHONCALL_LIBPTR: str
    JULIA_PYTHONCALL_EXE: str
    JULIA_CONDAPKG_EXE: str
    JULIA_CONDAPKG_BACKEND: str

    PYTHON_JULIACALL_SYSIMAGE: str
    PYTHON_JULIACALL_OPTIMIZE: str
    PYTHON_JULIACALL_COMPILE: str
    JULIA_DEPOT_PATH : str

    PATH: str
    HOME: str

    def __init__(self, env=None):
        self._env = env

    def add_path(self, s: str):
        sections = self.PATH.split(os.pathsep)
        if s not in sections:
            self.PATH = os.pathsep.join((s, *sections))

for varname in ENV.__annotations__:
    setattr(ENV, varname, env_descriptor(varname))

Environment = ENV()

def _setup():
    if Environment.JP_ADAPTOR_INITIALIZED:
        return

    Environment.PYTHON_JULIAPKG_OFFLINE = 'yes'
    Environment.JULIA_PYTHONCALL_LIBPTR = str(ctypes.pythonapi._handle)
    Environment.JP_ADAPTOR_PY_EXE = sys.executable

    #  setup julia executable path
    if not Environment.JP_ADAPTOR_JL_EXE:
        import subprocess
        import json
        config: dict[str, str] = json.loads(subprocess.check_output(['julia', '--startup-file=no', '--compile=min', '-O0', "-e", jl_info]).decode('utf-8').strip())
        Environment.JP_ADAPTOR_JL_EXE = config["julia_exe"]

        if not Environment.JP_ADAPTOR_JL_PROJ:
            Environment.JP_ADAPTOR_JL_PROJ = config["project"]
        if not Environment.JP_ADAPTOR_JL_IMAGE:
            Environment.JP_ADAPTOR_JL_IMAGE = config["sysimage"]
        if not Environment.JP_ADAPTOR_JL_DEPOT_PATH:
            Environment.JP_ADAPTOR_JL_DEPOT_PATH = config["depot_path"]

    # setup JuliaCall required environment variables
    if Environment.JP_ADAPTOR_JL_EXE:
        Environment.PYTHON_JULIAPKG_EXE = Environment.JP_ADAPTOR_JL_EXE
    if Environment.JP_ADAPTOR_JL_PROJ:
        Environment.JULIA_PYTHONCALL_PROJECT = Environment.PYTHON_JULIAPKG_PROJECT = Environment.JP_ADAPTOR_JL_PROJ
    if Environment.JP_ADAPTOR_JL_IMAGE:
        Environment.PYTHON_JULIACALL_SYSIMAGE = Environment.JP_ADAPTOR_JL_IMAGE


    # setup PythonCall required environment variables
    # not necessary because 'JULIA_PYTHONCALL_LIBPTR' is set
    if Environment.JP_ADAPTOR_CONDA_EXE:
        cond_path = Environment.JP_ADAPTOR_CONDA_EXE
        Environment.JULIA_CONDAPKG_EXE = cond_path
        Environment.JULIA_CONDAPKG_BACKEND = "System"
        Environment.add_path(os.path.dirname(cond_path))

    if Environment.JP_ADAPTOR_PY_EXE:
        py_path = Environment.JP_ADAPTOR_PY_EXE
        Environment.JULIA_PYTHONCALL_EXE = py_path
        Environment.add_path(os.path.dirname(py_path))

    # support user-specified julia depot paths
    if Environment.JP_ADAPTOR_JL_DEPOT_PATH:
        Environment.JULIA_DEPOT_PATH = Environment.JP_ADAPTOR_JL_DEPOT_PATH

    Environment.JP_ADAPTOR_INITIALIZED = "non_empty_string"

_setup()
