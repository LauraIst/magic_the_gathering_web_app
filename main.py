from typing import Optional

from fastapi import FastAPI
import requests

app = FastAPI()
rules_file = requests.get("https://media.wizards.com/2021/downloads/MagicCompRules%2020210419.txt").text

@app.get("/")
def read_root():
    return "This is Magic the Gathering project"


@app.get("/rules_file")
def read_rules():
    return rules_file

