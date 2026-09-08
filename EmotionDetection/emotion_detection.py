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
    result = {}
    mood_names = ("anger", "fear", "disgust", "sadness", "joy")
    max_mood_score = 0.0
    dominant_mood = None
    # Note that the assignment does not state what to do with status_code's
    # that are neither success (200) nor 400.
    if response.status_code == 400:
        for mood_name in mood_names:
            result[mood_name] = None
    else
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        for mood_name in mood_names:
            mood_score = emotions[mood_name]
            if mood_score > max_mood_score:
                max_mood_score = mood_score
                dominant_mood = mood_name
            result[mood_name] = mood_score
    result["dominant_emotion"] = dominant_mood
    return result
