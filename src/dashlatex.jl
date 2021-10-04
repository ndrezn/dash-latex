
module DashLatex
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.1.0"

include("jl/dashlatex.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_latex",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_latex.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_latex.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
