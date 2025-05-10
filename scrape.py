import bs4
import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, features="html.parser")

logos = soup.find_all("meta", property="og:image")
image_urls = [meta["content"] for meta in logos]
print(image_urls)

for i, url in enumerate(image_urls):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"image{i}.jpg", "wb") as file:
            file.write(response.content)
    else:
        print(f"Failed to download: {url}")
    