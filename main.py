from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from builders import make_table
from instamining import hashtag_minor
from wordcloud_gen import wordcloud_generator
import pandas as pd


# dash
stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    children=[
        dcc.Input(
            id="input-on-submit", type="text", placeholder="해시태그를 입력하세요."
        ),
        html.Button("Submit", id="submit", n_clicks=0),
        html.Div(id="hashtag-output"),
    ]
)


@app.callback(
    Output("hashtag-output", "children"),
    Input("submit", "n_clicks"),
    State("input-on-submit", "value"),
)
def update_output(n_clicks, value):
    # initial hashtag
    hashtag = value
    if "#" not in hashtag:
        hashtag = f"#{hashtag}"
    else:
        pass

    # hashtags mining and wordcloud generating
    hashtag_minor(hashtag)

    hashtag = hashtag.replace("#", "")

    wordcloud_generator(hashtag)

    hashtags_df = pd.read_csv(f"{hashtag}-report.csv").sort_values(
        by="Post Count", ascending=False
    )
    table = make_table(hashtags_df)
    img = html.Img(
        src=app.get_asset_url(f"{hashtag}-wordcloud.png"),
        style={"width": "300px", "height": "300px"},
    )
    return [img, table]


if __name__ == "__main__":
    app.run_server(debug=False)
