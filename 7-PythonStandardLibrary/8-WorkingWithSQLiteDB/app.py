import sqlite3
import json
from pathlib import Path

# Write to an sqlite db, sqlite3.connect("db.sqlite3") will try tio find db otherise creates it
data = Path("movies.json").read_text()

# movies = json.loads(data)


# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()


# Read from db

with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
