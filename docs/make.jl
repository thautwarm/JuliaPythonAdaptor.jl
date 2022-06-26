using JuliaPythonAdaptor
using Documenter

DocMeta.setdocmeta!(JuliaPythonAdaptor, :DocTestSetup, :(using JuliaPythonAdaptor); recursive=true)

makedocs(;
    modules=[JuliaPythonAdaptor],
    authors="thautwarm <twshere@outlook.com> and contributors",
    repo="https://github.com/thautwarm/JuliaPythonAdaptor.jl/blob/{commit}{path}#{line}",
    sitename="JuliaPythonAdaptor.jl",
    format=Documenter.HTML(;
        prettyurls=get(ENV, "CI", "false") == "true",
        canonical="https://thautwarm.github.io/JuliaPythonAdaptor.jl",
        edit_link="main",
        assets=String[],
    ),
    pages=[
        "Home" => "index.md",
    ],
)

deploydocs(;
    repo="github.com/thautwarm/JuliaPythonAdaptor.jl",
    devbranch="main",
)
