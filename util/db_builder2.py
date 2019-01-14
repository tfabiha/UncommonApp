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

# when you complete a puzzle, updates average moves for the player and for the puzzle itself
def updateAverageMovesUser(username,moves,puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    newMoves= getMovesUser(username) + moves
    numPlayed = getPuzzlePlayedUser(username) + 1
    newAverage = newMoves / numPlayed
    command = "UPDATE usersInfo SET moves = '" + str(newAverage) + "'WHERE users.username = '" + username + "';" #updates moves
    c.execute(command)
    db.commit()
    db.close()

# def addMovesUser(username,score):
#     DB_FILE="data/user.db"
#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()
#     command = "SELECT addMoves FROM usersInfo WHERE users.username ='" + username + "';" #selects score of the user
#     c.execute(command)
#     oldScore = c.fetchone()
#     newScore = oldScore[0] + score
#     command = "UPDATE users SET moves = '" + str(newScore) + "'WHERE users.username = '" + username + "';" #updates score
#     c.execute(command)
#     db.commit()
#     db.close()

def getMovesUser(username):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT moves FROM usersInfo WHERE usersInfo.username ='" + username + "';" #selects score of the user
    c.execute(command)
    oldScore = c.fetchone()[0]
    db.commit()
    db.close()
    return(oldScore)
print (getAverageMoves("user"))

def getPuzzlePlayedUser(username):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM logs WHERE logs.username ='" + username + "';" #selects score of the user
    c.execute(command)
    numPuzzlesDone = len(c.fetchall())
    return(numPuzzlesDone)

def updateAverageMovesPuzzle(moves,puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    newMoves= getMovesPuzzle(puzzleID) + moves
    numPlayed = getPuzzlePlayedPuzzle(puzzleID) + 1
    newAverage = newMoves / numPlayed
    command = "UPDATE puzzles SET moves = '" + str(newAverage) + "'WHERE puzzles.puzzleID = '" + puzzleID + "';" #updates moves
    c.execute(command)
    db.commit()
    db.close()

def getMovesPuzzle(puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT moves FROM puzzles WHERE puzzles.puzzleID ='" + puzzleID + "';" #selects score of the user
    c.execute(command)
    oldScore = c.fetchone()[0]
    db.commit()
    db.close()
    return(oldScore)

def getPuzzlePlayedPuzzle(puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM logs WHERE logs.puzzleID ='" + puzzleID + "';" #selects score of the user
    c.execute(command)
    numPuzzlesDone = len(c.fetchall())
    db.commit()
    db.close()
    return(numPuzzlesDone)

def addLikedPuzzle(user, puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzle_content FROM puzzles WHERE puzzles.puzzleID ='" + puzzleID + "';" #selects score of the user
    c.execute(command)
    puzzle_description = str(c.fetchall()[0])
    command = "UPDATE usersInfo SET likedPuzzles = '" + puzzle_description + "'WHERE usersInfo.username = '" + user + "';" #updates moves
    c.execute(command)
    db.commit()
    db.close()
s
