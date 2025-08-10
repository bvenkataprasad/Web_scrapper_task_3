import requests
url="https://www.bbc.com/news"
headers={"user-agent":"mozilla/5.0"}
response=requests.get(url,headers=headers)
html_content=response.text 
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_content,"html.parser")
headlines=soup.find_all("h2")
titles = [
    h.get_text(strip=True)     # Extract clean text
    for h in headlines         # Loop through all <h2> tags
    if h.get_text(strip=True)  # Keep only non-empty ones
]
with open("headlines.txt", "w", encoding="utf-8") as f:
    for title in titles:
        f.write(title + "\n")



