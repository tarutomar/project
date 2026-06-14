from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return sentiment, polarity, subjectivity


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    polarity = None
    subjectivity = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        sentiment, polarity, subjectivity = analyze_sentiment(text)

    return render_template(
        "index.html",
        text=text,
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity
    )


if __name__ == "__main__":
    app.run(debug=True)