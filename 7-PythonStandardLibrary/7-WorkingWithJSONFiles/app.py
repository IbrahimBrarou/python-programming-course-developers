import json
from pathlib import Path

# create json files from dictionearies

""" movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "kindergarten", "year": 1993}
]

Path("movies.json").write_text(json.dumps(movies)) """


# read json files
data = Path("movies.json").read_text()

movies = json.loads(data)
print(movies)
