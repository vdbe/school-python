#!/usr/bin/env python3
import sqlite3


def cmdsqlite(conn: sqlite3.Connection, query: str):
    cur = conn.execute(query)
    result = None
    if query.startswith("SELECT"):
        result = cur.fetchall()
    else:
        conn.commit()

    return result


def connecsqlite(path: str) -> sqlite3.connection:
    con = None
    try:
        con = sqlite3.connect(path)
        print("connected")

    except:
        print("connection error")
    finally:
        return con


queries = [
    """CREATE TABLE IF NOT EXISTS highscores (
	id INT AUTO_INCREMENT,
	name text NOT NULL,
	score INT,
	CONSTRAINT userrole_pk PRIMARY KEY(id)
);""",
    """INSERT INTO highscores (name, score) VALUES
    ('Alice', 20),
    ('Bob', 25),
    ('Carol', 23),
    ('Dave', 27),
    ('H4ck3r', 2000)
    """,
    """SELECT * FROM highscores WHERE score > 25""",
    """UPDATE highscores SET score=0 WHERE score > 100""",
    """DELETE FROM highscores WHERE name='H4CK3R'""",
    """SELECT * FROM highscores WHERE score > 25""",
]

conn = connecsqlite("highscores.sqlite")

for query in queries:
    cmdsqlite(conn, query)

conn.close()
