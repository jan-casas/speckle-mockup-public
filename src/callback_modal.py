import dash
from dash import html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
from app_initialization import dash_app
from pages.home import params


@dash_app.callback(
    Output("modal", "is_open"),
    Output("modal-body", "children"),
    Output("modal-info-title", "children"),
    [Input(f"more-info-{param['id']}", "n_clicks") for param in params],
    [State("modal", "is_open")]
)
def toggle_modal(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, "", ""
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    param_id = button_id.split("-")[-1]
    param = next((p for p in params if p["id"] == param_id), None)
    if param:
        modal_content = dbc.Row([
            dbc.Col(
                dbc.Container(
                    html.Iframe(src=param['src'], width="100%", height="100%",
                                style={'border': 'none'}),
                    style={'height': '100%'}
                ),
                width=6,
            ),
            dbc.Col(
                dbc.Row(html.Div(children=param['md'], style={'height': '100%'})),
                width=6,
                style={'maxHeight': 'calc(100vh - 210px)', 'overflowY': 'auto'}
            ),
        ])
        modal_title = dcc.Markdown(f"# {param['title']}")

        return not args[-1], modal_content, ""
    return args[-1], "", ""
