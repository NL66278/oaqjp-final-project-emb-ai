import unittest

from EmotionDetection import emotion_detection

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        input_versus_expected = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for case in input_versus_expected:
            result = emotion_detection.emotion_detector(case[0])
            self.assertEqual(result["dominant_emotion"], case[1])

unittest.main()
