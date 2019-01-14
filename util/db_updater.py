''' this file stores the updating ../database code'''

import sqlite3
from db_search import *
#from flask import request,session
'''
adduser(username,password)
params:username, password
username is the username of the user
password is the password of the user
function adds the username and password to the users ../database
'''
def adduser(username, password):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO usersInfo VALUES(?,?,?,?)"
    params=(username,password,0,"")
    c.execute(insert,params)
    db.commit()
    db.close()

#adduser("user1", "pass1")

def addPuzzle(puzzle_description):
    global puzzle_count
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO puzzles(puzzle_content,averageMoves) VALUES(?,?)"
    params=(puzzle_description,0)
    c.execute(insert,params)
    db.commit()
    db.close()

#addPuzzle("puzzle1")

def addLog(username,moves,puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO logs VALUES(?,?,?)"
    param = (username,moves,puzzleID)
    c.execute(command, param)
    db.commit()
    db.close()
# addLog("user1", 15, 1)
# addLog("user1", 20, 1)
# addLog("user1", 12, 1)


# when you complete a puzzle, updates average moves for the player and for the puzzle itself
def updateAverageMovesUser(username,moves,puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    newMoves= getMovesUser(username) + moves
    print (newMoves)
    numPlayed = getPuzzlePlayedUser(username) + 1.0
    print (numPlayed)
    newAverage = newMoves / numPlayed
    print (newAverage)
    command = "UPDATE usersInfo SET moves = '" + str(newAverage) + "'WHERE usersInfo.username = '" + username + "';" #updates moves
    c.execute(command)
    db.commit()
    db.close()
    return ("finished update average moves user")

print(updateAverageMovesUser("user1", 5, 1))

def updateAverageMovesPuzzle(moves,puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    newMoves= getMovesPuzzle(puzzleID) + moves
    numPlayed = getPuzzlePlayedPuzzle(puzzleID) + 1.0
    newAverage = newMoves / numPlayed
    command = "UPDATE puzzles SET averageMoves = '" + str(newAverage) + "'WHERE puzzles.puzzleID = '" + str(puzzleID) + "';" #updates moves
    c.execute(command)
    db.commit()
    db.close()
#print (updateAverageMovesPuzzle(12, 1))
print ("hi michelle")

def updatedLikedPuzzles(username, puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    list = getLikedPuzzles(username) + str(puzzleID) + ","
    command = "UPDATE usersInfo SET likedPuzzles = '" + str(list) + "'WHERE usersInfo.username = '" + username + "';" #updates moves
    c.execute(command)
    list  = c.fetchall()
    db.commit()
    db.close()
    return ("finished updatelikedpuzzles")
print(updatedLikedPuzzles("user1", 5))
print(":)")

print( updateAverageMovesPuzzle(15,1))
print(getMovesPuzzle("1"))
#print(getLikedPuzzles("user1"))
