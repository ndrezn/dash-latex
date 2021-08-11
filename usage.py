import dash_latex as dl
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("DashLatex: TeX input, HTML output test"),
        dl.DashLatex(
            r"""
            When $a \ne 0$, there are two solutions to \(ax^2 + bx + c = 0\) and they are
            $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
            """,
        ),
        html.H2("The Cauchy-Schwarz Inequality"),
        dl.DashLatex(
            r"""\[
            \left( \sum_{k=1}^n a_k b_k \right)^{\!\!2} \leq
            \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
            \]"""
        ),
        html.H2("A Cross Product Formula"),
        dl.DashLatex(
            r"""\[
            \mathbf{V}_1 \times \mathbf{V}_2 =
            \begin{vmatrix}
                \mathbf{i} &amp; \mathbf{j} &amp; \mathbf{k} \\
                \frac{\partial X}{\partial u} &amp; \frac{\partial Y}{\partial u} &amp; 0 \\
                \frac{\partial X}{\partial v} &amp; \frac{\partial Y}{\partial v} &amp; 0 \\
            \end{vmatrix}
            \]"""
        ),
        html.H2(
            dl.DashLatex(
                r"""The probability of getting \(k\) heads when flipping \(n\) coins is:"""
            ),
        ),
        dl.DashLatex(r"""\[P(E) = {n \choose k} p^k (1-p)^{ n-k} \]"""),
        html.H2("An Identity of Ramanujan"),
        dl.DashLatex(
            r"""\[
            \frac{1}{(\sqrt{\phi \sqrt{5}}-\phi) e^{\frac25 \pi}} =
                1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
                {1+\frac{e^{-8\pi}} {1+\ldots} } } }
            \]"""
        ),
        html.H2("In-line Mathematics"),
        dl.DashLatex(
            r"""Finally, while display equations look good for a page of samples, the
            ability to mix math and text in a paragraph is also important.  This
            expression $\sqrt{3x-1}+(1+x)^2$ is an example of an inline equation.  As
            you see, DashLatex equations can be used this way as well, without unduly
            disturbing the spacing between lines."""
        ),
        html.H2("Typeset as you go"),
        dcc.Textarea(
            id="latex-input",
            placeholder="Type to generate latex...",
            style={"width": "40%", "height": 150},
        ),
        html.Div(id="dynamic-latex", style={"margin": "5px"}),
    ]
)


@app.callback(
    Output("dynamic-latex", "children"),
    Input("latex-input", "value"),
)
def update_latex(value):
    if value:
        return dl.DashLatex(f"\\[{value}\\]")


if __name__ == "__main__":
    app.run_server(debug=True)
