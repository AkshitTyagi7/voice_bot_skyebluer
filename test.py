import http.client
import json

conn = http.client.HTTPConnection("localhost", 8000)
payload = json.dumps({
    "message": "repeat the qquestion"
})
headers = {
    'Content-Type': 'application/json'
}
conn.request("POST", "/chatbot", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
