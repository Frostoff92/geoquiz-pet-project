import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "countries.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    COUNTRIES = json.load(file)