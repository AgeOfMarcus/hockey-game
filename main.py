#!/usr/bin/python3

import sqlite3, uuid, time
from termcolor import colored as c # because who can be bothered to type "termcolor.colored"
from random import randint

db = sqlite3.connect("hockey.db")
cursor = db.cursor()


