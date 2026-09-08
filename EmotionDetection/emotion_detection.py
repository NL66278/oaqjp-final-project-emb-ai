"""Final project for Coursera AI based web application development."""
import json
import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network"
    "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    """Analyze emotions in the text passed."""
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=input_json, headers=HEADERS)
    formatted_response = json.loads(response.text)
    result = {}
    max_mood_score = 0.0
    dominant_mood = None
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    mood_names = ("anger", "fear", "disgust", "sadness", "joy")
    for mood_name in mood_names:
        mood_score = emotions[mood_name]
        if mood_score > max_mood_score:
            max_mood_score = mood_score
            dominant_mood = mood_name
        result[mood_name] = mood_score
    result["dominant_emotion"] = dominant_mood
    return result
