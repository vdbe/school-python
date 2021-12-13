#!/usr/bin/env python3
import sqlite3


def connecsqlite(path: str) -> sqlite3.Connection:
    con = None
    try:
        con = sqlite3.connect(path)
        print("Connected")

    except:
        print("Connection Error")
    finally:
        return con
