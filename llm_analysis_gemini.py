from urllib import response
import pandas as pd

df = pd.read_csv('bid_scraper\\bids.csv')
# print(df.head())

prompts = []

for idx, row in df.iterrows():
    prompt = (
        f"Bid Title: {row['title']}\n"
        f"URL: {row['url']}\n"
        f"Expiration Date: {row['expiration_date']}\n"
        f"Publish Date: {row['publish_date']}\n"
        f"Category: {row['category']}\n"
        f"Solicitation Type: {row['solicitation_type']}\n"
        f"Issuing Agency: {row['issuing_agency']}\n"
        "Please analyze this bid and provide insights."
    )
    prompts.append(prompt)

import requests

import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent'
def gemini_call(prompt):
    headers = {"Content-Type": "application/json"}

    body = {
        "contents": [{"parts": [{"text":prompt}]}]
    }

    params = {
        "key" : GEMINI_API_KEY
    }

    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=body)
    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

for prompt in prompts[:5]:
    result = gemini_call(prompt)
    print("Gemini analysis result:\n", result)