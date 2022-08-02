import unittest
import http.client
import json


class TestAPIChatBot(unittest.TestCase):
    def test_chatbot_success(self):

        conn = http.client.HTTPConnection("localhost", 8000)
        payload = json.dumps({
            "message": "hi"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/chatbot", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        self.assertIsInstance(data.get("result", None), str)
