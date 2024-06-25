import json
from pathlib import Path


movies = [
    {"id": 1, "title": "Phantom Menace", "year": 1999},
    {"id": 2, "title": "Attack of Clones", "year": 2001},
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[1]["title"])