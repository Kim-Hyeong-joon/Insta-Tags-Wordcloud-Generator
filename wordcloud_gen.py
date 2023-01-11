import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def wordcloud_generator(hashtag):
    hashtags_df = pd.read_csv(f"{hashtag}-report.csv")
    wordcloud = WordCloud(
        font_path="font/NotoSansKR-Regular.ttf",
        width=800,
        height=800,
        background_color="white",
        prefer_horizontal=0.9999,
    )

    frequencies = hashtags_df.set_index("Hastag").to_dict()["Post Count"]

    keyword = wordcloud.generate_from_frequencies(frequencies)

    array = keyword.to_array()

    plt.figure(figsize=(10, 10), frameon=False)
    plt.imshow(array, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("wordcloud.png")
