from instamining import hashtag_minor
from wordcloud_gen import wordcloud_generator

hashtag = "dog"
if "#" not in hashtag:
    hashtag = f"#{hashtag}"


hashtag_minor(hashtag)
hashtag = hashtag.replace("#", "")
wordcloud_generator(hashtag)
