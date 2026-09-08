"""Serve the emotion detection as a Flask Web app."""
from flask import Flask, request, render_template

from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detection.emotion_detector(text_to_analyze)
    return (
        "For the given statement, the system response is"
        f" 'anger': {result['anger']},"
        f" 'disgust': {result['disgust']},"
        f" 'fear': {result['fear']},"
        f" 'joy': {result['joy']} and"
        f" 'sadness': {result['sadness']}."
        f" The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run()
