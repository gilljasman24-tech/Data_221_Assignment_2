import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the main content area
content = soup.find("div", id="mw-content-text")

# Find all h2 headings inside the content
headings = content.find_all("h2")

excluded_words = ["References", "External links", "See also", "Notes"]

clean_headings = []

for h in headings:
    text = h.get_text().replace("[edit]", "").strip()

    # Skip excluded headings
    if any(word in text for word in excluded_words):
        continue

    clean_headings.append(text)

# Save headings to a text file
file = open("headings.txt", "w", encoding="utf-8")
for heading in clean_headings:
    file.write(heading + "\n")
file.close()

# Print confirmation
print("Saved", len(clean_headings), "headings to headings.txt")