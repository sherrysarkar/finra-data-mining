import json
from pathlib import Path

dataDir = Path('../data/court-opinions').resolve()

keywords = []  # replace with real keywords
documents = []
for file in dataDir.iterdir():
    with file.open('r') as f:
        text = json.load(f)['plain_text'].replace('\n', '')



