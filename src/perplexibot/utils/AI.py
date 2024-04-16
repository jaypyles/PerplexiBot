# STL
import asyncio
import json

import aiohttp
# PDM
import requests


async def call_search(prompt: str) -> dict:
    url = "http://searchbackend:8000/api/search/get_search_refs"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    data = {
        "query": prompt,
        "model": "gpt3.5",
        "ask_type": "search",
        "llm_auth_token": "",
        "llm_base_url": None,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            response_text = await response.json()
            return response_text


def call_research(prompt: str):
    body = {
        "model": "gpt3.5",
        "messages": [{"role": "user", "content": prompt}],
    }

    url = "http://searchbackend:8000/v1/chat/completions"
    total_content = ""
    response = requests.post(url, json=body)
    response_text = response.text
    data_chunks = response_text.split("\n")

    total_content = ""
    for chunk in data_chunks:
        if chunk:
            print(f"Chunk: {chunk}")
            clean_json = chunk.replace("data: ", "")
            try:
                if clean_json:
                    dict_data = json.loads(clean_json)
                    token = dict_data["choices"][0]["delta"].get("content", "")
                    if token:
                        total_content += token
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e} - Chunk: {clean_json}")

    return total_content
