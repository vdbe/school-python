#!/usr/bin/env python3
import sqlite3


def cmdsqlite(conn: sqlite3.Connection, query: str):
    conn.execute(query)
    result = None
    if query.startswith("SELECT"):
        result = conn.fetchall()
    else:
        conn.commit()

    return result
