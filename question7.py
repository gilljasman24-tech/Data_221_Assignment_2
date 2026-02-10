import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

# Add a user-agent so Wikipedia allows the request
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Print the page title
print("Page title:")
print(soup.title.get_text(strip=True))
print()

# Find main content
content = soup.find("div", id="mw-content-text")
paragraphs = content.find_all("p")

# Print the first paragraph with at least 50 characters
for p in paragraphs:
    text = p.get_text().strip()
    if len(text) >= 50:
        print("First paragraph:")
        print(text)
        break
