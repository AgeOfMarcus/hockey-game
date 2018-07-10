#!/usr/bin/python3

import sqlite3, uuid, time, os
from termcolor import colored as c # because who can be bothered to type "termcolor.colored"
from random import randint

# Useful functions
def clear(): a = os.system("clear")

db = sqlite3.connect("hockey.db")
cursor = db.cursor()

# Setting up the database and tables
cursor.execute("CREATE TABLE IF NOT EXISTS players (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT NOT NULL, TEAM TEXT NOT NULL, ATK INT NOT NULL, DEF INT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS scores (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, TEAM1 TEXT NOT NULL, TEAM2 TEXT NOT NULL, SCORE TEXT NOT NULL)")

# Adding player functions
def add_player(name,team,atk,def_):
	cmd = "INSERT INTO players (NAME, TEAM, ATK, DEF) VALUES ('%s','%s',%s,%s)" % (name,team,atk,def_)
	cursor.execute(cmd)
	db.commit()





if __name__ == "__main__":
	import code; code.interact(local=dict(globals(), **locals())) #debug
	db.commit()
	db.close()
