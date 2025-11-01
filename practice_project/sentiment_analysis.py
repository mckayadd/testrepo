from textblob import TextBlob

def sentiment_analyzer(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # range: -1 (negative) → +1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) → 1 (subjective)

    if polarity > 0:
        label = "Positive"
    elif polarity < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return {"label": label, "polarity": polarity, "subjectivity": subjectivity}


if __name__ == "__main__":
    result = sentiment_analyzer("I love to study!")
    print(result)
