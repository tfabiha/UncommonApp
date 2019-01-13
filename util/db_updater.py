''' this file stores the updating ../database code'''

import sqlite3
#from flask import request,session
'''
adduser(username,password)
params:username, password
username is the username of the user
password is the password of the user
function adds the username and password to the users ../database
'''
def adduser(username, password):
    DB_FILE="data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO usersInfo VALUES(?,?,?,?)"
    params=(username,password,0,"")
    c.execute(insert,params)
    db.commit()
    db.close()
adduser("user", "pass")
print("added user")

def addPuzzle(puzzle_description):
    global puzzle_count
    DB_FILE="data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO puzzles(puzzle_content,averageMoves) VALUES(?,?)"
    params=(puzzle_description,0)
    c.execute(insert,params)
    db.commit()
    db.close()
addPuzzle("addapuzzle")
print("added puzzle")

'''
addScore(username,score):
params:username, score
username is the username of the user in session
moves is the point value of the question added
function adds the point value of the question to the users score
'''

command = "CREATE TABLE logs(username TEXT, moves INTEGER, puzzleID INTEGER)"

def addLog(username,moves,puzzleID):
    DB_FILE="data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO logs VALUES(?,?,?)"
    param = (username,moves,puzzleID)
    c.execute(command, param)

#    command = "UPDATE users SET moves = '" + str(newScore) + "'WHERE users.username = '" + username + "';" #updates score
    db.commit()
    db.close()

addLog("hi", 2, 4)
print("addlog")
'''
subScore(username,score):
params:username, score
username is the username of the user in session
score is the point value of the question added
function subtracts the point value of the question from the users score
'''
def subScore(username, score):
    addScore(username, score * -1)

'''
ansQuestion(username, question, answer)
params:username, question, answer
username is the username of the user in session
question is the question the user answered
answer is api provided answer for the question
'''

def ansQuestion(username, question):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO questions VALUES(?,?)"
    params = (username, question)
    c.execute(insert, params)
    db.commit()
