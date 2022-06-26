using JuliaPythonAdapator
using Documenter

DocMeta.setdocmeta!(JuliaPythonAdapator, :DocTestSetup, :(using JuliaPythonAdapator); recursive=true)

makedocs(;
    modules=[JuliaPythonAdapator],
    authors="thautwarm <twshere@outlook.com> and contributors",
    repo="https://github.com/thautwarm/JuliaPythonAdapator.jl/blob/{commit}{path}#{line}",
    sitename="JuliaPythonAdapator.jl",
    format=Documenter.HTML(;
        prettyurls=get(ENV, "CI", "false") == "true",
        canonical="https://thautwarm.github.io/JuliaPythonAdapator.jl",
        edit_link="main",
        assets=String[],
    ),
    pages=[
        "Home" => "index.md",
    ],
)

deploydocs(;
    repo="github.com/thautwarm/JuliaPythonAdapator.jl",
    devbranch="main",
)
