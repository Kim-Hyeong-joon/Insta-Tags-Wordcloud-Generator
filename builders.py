import dash_html_components as html


def make_table(df):
    return html.Table(
        style={"width": 500},
        children=[
            html.Thead(
                style={
                    "display": "block",
                    "marginBottom": 25,
                },
                children=[
                    html.Tr(
                        children=[
                            html.Th(column_name.replace("_", " "))
                            for column_name in df.columns
                        ],
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(2, 1fr)",
                            "fontWeight": "600",
                            "fontSize": 14,
                        },
                    )
                ],
            ),
            html.Tbody(
                style={
                    "maxHeight": "50vh",
                    "display": "block",
                    "overflow": "scroll",
                },
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(2, 1fr)",
                            "border-top": "1px solid white",
                            "padding": "30px 0px",
                        },
                        children=[
                            html.Td(
                                value_column, style={"textAlign": "center"}
                            )
                            for value_column in value
                        ],
                    )
                    for value in df.values
                ],
            ),
        ],
    )
