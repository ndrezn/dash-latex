# AUTO GENERATED FILE - DO NOT EDIT

dashLatex <- function(children=NULL, id=NULL, displayMode=NULL, errorColor=NULL, fleqn=NULL, globalGroup=NULL, leqno=NULL, macros=NULL, maxExpand=NULL, maxSize=NULL, minRuleThickness=NULL, strict=NULL, throwOnError=NULL) {
    
    props <- list(children=children, id=id, displayMode=displayMode, errorColor=errorColor, fleqn=fleqn, globalGroup=globalGroup, leqno=leqno, macros=macros, maxExpand=maxExpand, maxSize=maxSize, minRuleThickness=minRuleThickness, strict=strict, throwOnError=throwOnError)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashLatex',
        namespace = 'dash_latex',
        propNames = c('children', 'id', 'displayMode', 'errorColor', 'fleqn', 'globalGroup', 'leqno', 'macros', 'maxExpand', 'maxSize', 'minRuleThickness', 'strict', 'throwOnError'),
        package = 'dashLatex'
        )

    structure(component, class = c('dash_component', 'list'))
}
