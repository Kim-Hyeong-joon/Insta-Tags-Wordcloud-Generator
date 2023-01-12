from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from instamining import hashtag_minor
from builders import make_table
from wordcloud_gen import wordcloud_generator
import pandas as pd
import plotly.express as px


# dash
stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    children=[
        html.Div(
            style={
                "width": "100%",
                "text-align": "center",
                "margin-top": "20px",
            },
            children=[
                dcc.Input(
                    id="input-on-submit",
                    type="text",
                    placeholder="해시태그를 입력하세요.",
                ),
                html.Button("검색", id="submit", n_clicks=0),
            ],
        ),
        html.Div(
            style={"display": "grid", "gridTemplateColumns": "1fr 1fr"},
            id="hashtag-output",
        ),
    ]
)


@app.callback(
    Output("hashtag-output", "children"),
    Input("submit", "n_clicks"),
    State("input-on-submit", "value"),
)
def update_output(n_clicks, value):
    if n_clicks is None:
        raise PreventUpdate
    # initial hashtag
    hashtag = value
    if "#" not in hashtag:
        hashtag = f"#{hashtag}"
    else:
        pass

    # hashtags mining, create csv file and wordcloud generating
    hashtag_minor(hashtag)

    hashtag = hashtag.replace("#", "")

    wordcloud_generator(hashtag)
    # hashtags df
    hashtags_df = pd.read_csv(f"{hashtag}-report.csv").sort_values(
        by="Post Count", ascending=False
    )
    # elements
    table = make_table(hashtags_df)
    img = html.Img(
        src=app.get_asset_url(f"{hashtag}-wordcloud.png"),
        style={"width": "100%", "height": "100%"},
    )
    bars_graph = px.bar(
        hashtags_df,
        x="Hashtag",
        y="Post Count",
        template="plotly_dark",
        title=f"{value} hashtags",
    )
    graph = dcc.Graph(
        figure=bars_graph, style={"gridColumn": "span 2", "margin": "20px"}
    )
    return [graph, img, table]


if __name__ == "__main__":
    app.run_server(debug=False)
