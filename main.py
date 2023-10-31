import requests
from send_email import  sendEmail

topic = "tesla"

api_key = "c09363f8c9de4490a35752416fed9236"
url = "https://newsapi.org/v2/everything?"\
        f"q={topic}&" \
        "from=2023-09-30&"\
        "sortBy=publishedAt"\
        "&apiKey=c09363f8c9de4490a35752416fed9236&"\
        "language=en"

request = requests.get(url)
content = request.json()

body = "Subject: Today's news\n"
for article in content["articles"][:20]:
    title = article["title"]
    author = article["author"]
    news_url = article["url"]

    if author is not None:
        body = (body + title + "\n" + author + "\n" + news_url + 2*"\n")

print(content["articles"])

body = body.encode("utf-8")
sendEmail(message=body)
