import json
from processor import process_threats

with open("sample_input.json") as f:
    data = json.load(f)

process_threats(data["threats"])

