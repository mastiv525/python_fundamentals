import json
from pathlib import Path


movies = [
    {"id": 1, "title": "Phantom Menace", "year": 1999},
    {"id": 2, "title": "Attack of the Clones", "year": 2002},
    {"id": 3, "title": "Revenge of the Sith", "year": 2005},
    {"id": 4, "title": "A New Hope", "year": 1977},
    {"id": 5, "title": "Phantom Menace", "year": 1980},
    {"id": 6, "title": "Phantom Menace", "year": 1983},
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[1]["title"])