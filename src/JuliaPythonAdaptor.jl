module JuliaPythonAdaptor
import Pkg

@nospecialize

if isdefined(Base, :Experimental) && isdefined(Base.Experimental, Symbol("@compiler_options"))
    Base.Experimental.@compiler_options optimize=0 compile=min infer=no
end

function setenv!(varname::String, value::AbstractString)
    ENV[varname] = value
end

function getenv(varname::String)
    get(ENV, varname, "")
end

function hasenv(varname::String)
    haskey(ENV, varname)
end

function found_key(f, d, key)
    if haskey(d, key)
        f(d[key])
        return true
    end
    return false
end

function __init__()
    if hasenv("JP_ADAPTOR_INITIALIZED")
        return
    end

    setenv!("JP_ADAPTOR_JL_DEPOT_PATH", DEPOT_PATH[1])
    setenv!("JP_ADAPTOR_JL_PROJ", dirname(Pkg.project().path))
    setenv!("JP_ADAPTOR_JL_EXE", Base.julia_cmd().exec[1])
    setenv!("JP_ADAPTOR_JL_IMAGE", unsafe_string(Base.JLOptions().image_file))
    setenv!("JULIA_PYTHONCALL_PROJECT", getenv("JP_ADAPTOR_JL_PROJ"))

    if !hasenv("JP_ADAPTOR_PY_EXE")
        python = Sys.which("python")
        if !isnothing(python)
            setenv!("JP_ADAPTOR_PY_EXE", python)
        end
    end

    if !hasenv("JP_ADAPTOR_CONDA_EXE")
        for conda_exe_name in ["conda", "mamba", "micromamba"]
            conda = Sys.which("conda")
            if isnothing(conda)
                continue
            end
            setenv!("JP_ADAPTOR_CONDA_EXE", conda)
            break
        end
    end

    setenv!("PYTHON_JULIAPKG_EXE", getenv("JP_ADAPTOR_JL_EXE"))
    setenv!("PYTHON_JULIAPKG_PROJECT", getenv("JP_ADAPTOR_JL_PROJ"))
    setenv!("PYTHON_JULIACALL_SYSIMAGE", getenv("JP_ADAPTOR_JL_IMAGE"))
    setenv!("PYTHON_JULIAPKG_OFFLINE", "yes")

    if hasenv("JP_ADAPTOR_PY_EXE")
        setenv!("JULIA_PYTHONCALL_EXE", getenv("JP_ADAPTOR_PY_EXE"))
    end
    
    # XXX: This makes no sense now.
    # After resolving https://github.com/cjdoris/CondaPkg.jl/issues/2
    # it will be possible for us to use an existing conda environment.
    if hasenv("JP_ADAPTOR_CONDA_EXE")
        setenv!("JULIA_CONDAPKG_EXE", getenv("JP_ADAPTOR_CONDA_EXE"))
        setenv!("JULIA_CONDAPKG_BACKEND", "System")
    end

    setenv!("JP_ADAPTOR_JL_DEPOT_PATH", getenv("JP_ADAPTOR_JL_DEPOT_PATH"))

    setenv!("JP_ADAPTOR_INITIALIZED", "non_empty_string")
end

end
