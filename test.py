import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"title": "India won the T20 world cup", "summary": "India won the world cup with a tough fight in T20.", "srcLink": "http://newsarticle.com"},
    {"title": "Nvidia stocks reached market high", "summary": "Nvidia stocks became the most valuable stocks exceeding the Alphabet stocks", "srcLink": "http://newsarticle.com"},
    {"title": "Self-driving cars Operational in US", "summary": "Now you can go on a rider without a driver. Self-driving cars are operational in US", "srcLink": "http://newsarticle.com"},
]

for i in range(len(data)):
 response = requests.post(BASE + "shorts/"+ str(i), data[i])
 print(response)

input()
response = requests.delete(BASE + "shorts/0")
print(response)
input()

response = requests.get(BASE + "shorts/6")
print(response)

