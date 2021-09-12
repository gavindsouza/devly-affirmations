import json
import os
import random
from typing import Dict, List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_file_path(*path):
    return os.path.join(os.path.dirname(__file__), *path)


with open(get_file_path("affirmations", "affirmations.json")) as f:
    affirmation_list: List = json.loads(f.read())

with open(get_file_path("static", "page.html")) as f:
    html_content: str = f.read()


async def fetch_page_content() -> str:
    affirmation = random.choice(affirmation_list)
    author, quote = affirmation["author"], affirmation["affirmation"]

    return html_content.replace(
        "affirmation: null,", f"affirmation: '{quote}',"
    ).replace("author: null,", f"author: '{author}',")


@app.get("/")
@app.get("/author/{author}")
async def quote(author: str = None) -> Dict:
    if author:
        author_list = list(filter(lambda x: x["author"] == author, affirmation_list))
    else:
        author_list = affirmation_list

    return random.choice(author_list)


@app.get("/quotes")
async def all_quotes() -> List:
    return affirmation_list


@app.get("/authors")
async def all_authors() -> List:
    return set(x["author"] for x in affirmation_list)


@app.get("/devly-affirmations", response_class=HTMLResponse)
async def render_page():
    html_content = await fetch_page_content()
    return HTMLResponse(content=html_content)
