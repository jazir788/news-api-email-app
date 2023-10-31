import requests

api_key = "c09363f8c9de4490a35752416fed9236"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-09-30&"\
       "sortBy=publishedAt&apiKey=c09363f8c9de4490a35752416fed9236")

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["author"])
