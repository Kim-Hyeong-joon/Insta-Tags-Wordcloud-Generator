import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def wordcloud_generator(df):
    wordcloud = WordCloud(
        font_path="font/NotoSansKR-Regular.ttf",
        width= 800,
        height= 800,
        background_color="white",
        prefer_horizontal = 0.9999
    )

    frequencies = df.set_index("keyword").to_dict()['count']

    keyword = wordcloud.generate_from_frequencies(frequencies)

    array = keyword.to_array()

    plt.figure(figsize=(10,10), frameon=False)
    plt.imshow(
        array,
        interpolation="bilinear"
    )
    plt.axis("off")

plt.savefig("wordcloud.png")