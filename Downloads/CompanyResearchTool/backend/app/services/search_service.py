import requests
import os

from dotenv import load_dotenv

load_dotenv()


def search_company(company_name: str):

    url = "https://google.serper.dev/search"

    payload = {
        "q": company_name
    }

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.json()