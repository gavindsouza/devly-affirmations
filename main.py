import json
import os
import random

from flask import Flask

app = Flask(__name__)


def get_file_path(*path):
    return os.path.join(os.path.dirname(__file__), *path)


with open(get_file_path("affirmations", "affirmations.json")) as f:
    affirmation_list: list = json.loads(f.read())


@app.get("/")
@app.get("/author/{author}")
def quote(author: str = None) -> dict:
    if author:
        author_list = [x for x in affirmation_list if x["author"] == author]
    else:
        author_list = affirmation_list

    return random.choice(author_list)


@app.get("/quotes")
def all_quotes() -> list:
    return affirmation_list


@app.get("/authors")
def all_authors() -> list:
    return list({x["author"] for x in affirmation_list})
