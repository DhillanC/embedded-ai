""" Unit test file for EmotionDetection package"""
import unittest
from unittest.mock import patch
from emotion_detection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy_emotion_detector(self):
        """Test case for joy emotion"""
        # Call the emotion detector function with a joyful text
        result = emotion_detector('I am glad this happened')
        # Assert that the dominant emotion is 'joy'
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion_detector(self):
        """Test case for anger emotion"""
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

    def test_disgust_emotion_detector(self):
        """Test case for disgust emotion"""
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

    def test_sadness_emotion_detector(self):
        """Test case for sadness emotion"""
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

    def test_fear_emotion_detector(self):
        """Test case for fear emotion"""
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

    def test_empty_text(self):
        """Test case for an empty text."""
        # No need to mock a response since no request will be made for empty text
        result = emotion_detector('')

        # Assert that the dominant emotion and all emotions are None
        self.assertEqual(result['dominant_emotion'], None)
        self.assertEqual(result['joy'], None)

    @patch('Emotion_Detection.emotion_detection.requests.post')
    def test_mock_joy_emotion_detector(self, mock_post):
        """Mock test case for joy emotion"""
        # Mocking the API response for joy
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'emotionPredictions': [
                {'emotion': {'joy': 0.9, 'anger': 0.05, 'disgust': 0.02, 'fear': 0.02, 'sadness': 0.01}}
            ]
        }
        # Call the emotion detector function with a joyful text
        result = emotion_detector('I am glad this happened')

        # Assert that the dominant emotion is 'joy'
        self.assertEqual(result['dominant_emotion'], 'joy')

        # Assert that the joy score is correct
        self.assertAlmostEqual(result['joy'], 0.9)

unittest.main()
