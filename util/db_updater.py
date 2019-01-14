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
#    command = "UPDATE users SET moves = '" + str(newScore) + "'WHERE users.username = '" + username + "';" #updates score
    db.commit()
    db.close()
# addLog("user1", 15, 1)
# addLog("user1", 20, 1)
# addLog("user1", 12, 1)

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
#print (getAverageMoves("user"))

def getPuzzlePlayedUser(username):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM logs WHERE logs.username ='" + username + "';" #selects score of the user
    c.execute(command)
    numPuzzlesDone = len(c.fetchall())
    return(numPuzzlesDone)

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



def getMovesPuzzle(puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT averageMoves FROM puzzles WHERE puzzles.puzzleID ='" + str(puzzleID) + "';" #selects score of the user
    c.execute(command)
    oldScore = c.fetchone()[0]
    db.commit()
    db.close()
    return(oldScore)

def getPuzzlePlayedPuzzle(puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM logs WHERE logs.puzzleID ='" + str(puzzleID)+ "';" #selects score of the user
    c.execute(command)
    numPuzzlesDone = len(c.fetchall())
    db.commit()
    db.close()
    return(numPuzzlesDone)

def updateAverageMovesPuzzle(moves,puzzleID):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    newMoves= getMovesPuzzle(puzzleID) + moves
    numPlayed = getPuzzlePlayedPuzzle(puzzleID) + 1
    newAverage = newMoves / numPlayed
    command = "UPDATE puzzles SET averageMoves = '" + str(newAverage) + "'WHERE puzzles.puzzleID = '" + str(puzzleID) + "';" #updates moves
    c.execute(command)
    db.commit()
    db.close()
print (updateAverageMovesPuzzle(12, 1))
print ("hi michelle")



def getLikedPuzzles(username):
    DB_FILE="../data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT likedPuzzles FROM usersInfo WHERE usersInfo.username ='" + username + "';" #selects score of the user
    c.execute(command)
    list  = c.fetchall()
    print(list[0])
    db.commit()
    db.close()
    return (list[0][0])
    #return ("finished getlikedpuzzles")
print(getLikedPuzzles("user1"))

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
print(getLikedPuzzles("user1"))
