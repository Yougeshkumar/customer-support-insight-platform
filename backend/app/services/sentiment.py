from textblob import TextBlob


def analyze_sentiment(message: str):
    polarity = TextBlob(message).sentiment.polarity

    if polarity <= -0.3:
        frustration = "High"
    elif polarity <= 0.1:
        frustration = "Medium"
    else:
        frustration = "Low"

    return round(polarity, 3), frustration