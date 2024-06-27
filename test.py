import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE+"shorts/4", {"title": "Gold prices reach all time high", "summary": "Amid market uncertainities gold prices reach all time high", "srcLink": "http://newsarticle.com"})
print(response.json())

input()

response = requests.get(BASE+"shorts/1")
print(response.json())

