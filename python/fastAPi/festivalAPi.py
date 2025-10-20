import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


def extract_festivals(search_html):
    soup = BeautifulSoup(search_html, 'html.parser')
    results = []

    for div in soup.find_all("div", {"class": "tF2Cxc"}):
        title = div.find("h3").text
        results.append(title)

    return results

@app.get("/get_festivals/")
async def get_festivals(year: int):
    query = f"{year} festivals"
    search_html = google_search(query)

    if search_html:
        festivals = extract_festivals(search_html)
        if festivals:
            return {"Year": year, "Festivals": festivals}
        else:
            return {"error": "No festivals found in the search results."}
    else:
        return {"error": "Failed to retrieve search results."}
@app.get("/wishyou/")
async def wishyou():
    return {"message": "Wishing you a joyful festival season!"}
