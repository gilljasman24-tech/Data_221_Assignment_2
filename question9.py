import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", id="mw-content-text")
tables = content.find_all("table")

rows = []
selected_table = None

# Find the first usable table
for table in tables:
    # Skip navigation boxes
    if "navbox" in table.get("class", []):
        continue

    table_rows = table.find_all("tr")

    # Need at least header + 3 data rows
    if len(table_rows) < 4:
        continue

    # Must have at least 2 columns
    cells = table_rows[1].find_all(["td", "th"])
    if len(cells) < 2:
        continue

    selected_table = table
    rows = table_rows
    break

# Safety check (should never fail now, but required)
if not rows:
    raise RuntimeError("No suitable table found on the page.")

# Extract headers
header_cells = rows[0].find_all("th")

if header_cells:
    headers_list = [cell.get_text(strip=True) for cell in header_cells]
else:
    num_cols = len(rows[1].find_all("td"))
    headers_list = [f"col{i+1}" for i in range(num_cols)]

data = []

# Extract data rows
for row in rows[1:]:
    cells = row.find_all(["td", "th"])
    row_data = [cell.get_text(strip=True) for cell in cells]

    while len(row_data) < len(headers_list):
        row_data.append("")

    data.append(row_data)

# Save to CSV
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers_list)
    writer.writerows(data)
