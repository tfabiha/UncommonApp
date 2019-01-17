''' this file stores the updating database code'''

import sqlite3
from util import db_search as search

#from db_search import *
#from flask import request,session
'''
adduser(username,password)
params:username, password
username is the username of the user
password is the password of the user
function adds the username and password to userInfo
'''
def adduser(username, password):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO usersInfo VALUES(?,?,?,?)"
    params=(username,password,0,"")
    c.execute(insert,params)
    db.commit()
    db.close()

'''
addPuzzle(puzzle_description, moves)
params:puzzle_description, moves
puzzle_description is how puzzles are represent in the format of {length, width, corner1color, c2c, c3c, c4c}
moves is how many moves the first player took to solve the puzzle
function adds the puzzle_description and moves to the database and assigns it an ID
'''
def addPuzzle(puzzle_description, moves):
    global puzzle_count
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    insert = "INSERT INTO puzzles(puzzle_content,averageMoves) VALUES(?,?)"
    params=(puzzle_description, moves)
    c.execute(insert,params)
    db.commit()
    db.close()

# addPuzzle("puzzle1",0)
# addPuzzle("puzzle2",0)
# addPuzzle("puzzle3",0)
# addPuzzle("puzzle4",0)
# print("hi")
'''
addLog(username,moves,puzzleID)
params:username,moves,puzzleID
username: the user who has solved the puzzle
moves: the number of moves they took to complete a given puzzle
puzzleID: the id of the puzzle that was created
function adds the a new log to the logs database (tracking history)
'''
def addLog(username,moves,puzzleID):
    DB_FILE="./data/uncommonApp.db"
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

'''
updateAverageMovesUser(username,moves,puzzleID)
params:username,moves,puzzleID
username: the user who has solved the puzzle
moves: the number of moves they took to complete a given puzzle
puzzleID: the id of the puzzle that was just solved
function updates the average moves a user takes to complete all of his/her puzzles
'''
# when you complete a puzzle, updates average moves for the player and for the puzzle itself
def updateAverageMovesUser(username,moves,puzzleID):
    DB_FILE="./data/uncommonApp.db"
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

#print(updateAverageMovesUser("user1", 5, 1))

'''
updateAverageMovesPuzzle(moves,puzzleID)
params:moves,puzzleID
moves: the number of moves they took to complete a given puzzle
puzzleID: the id of the puzzle that was just solved
function updates the average moves a user takes to complete a given puzzle
'''
def updateAverageMovesPuzzle(moves,puzzleID):
    DB_FILE="./data/uncommonApp.db"
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
#print ("hi michelle")

# '''
# updatedLikedPuzzles(username, puzzleID)
# params:username,puzzleID
# moves: the number of moves they took to complete a given puzzle
# puzzleID: the id of the puzzle that was just solved
# function updates the average moves a user takes to complete a given puzzle
# '''
# def updatedLikedPuzzles(username, puzzleID):
#     DB_FILE="./data/uncommonApp.db"
#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()
#     list = getLikedPuzzles(username) + str(puzzleID) + ","
#     command = "UPDATE usersInfo SET likedPuzzles = '" + str(list) + "'WHERE usersInfo.username = '" + username + "';" #updates moves
#     c.execute(command)
#     list  = c.fetchall()
#     db.commit()
#     db.close()
#     return ("finished updatelikedpuzzles")
# print(updatedLikedPuzzles("user1", 5))
# print(":)")
#
# print( updateAverageMovesPuzzle(15,1))
# print(getMovesPuzzle("1"))
# #print(getLikedPuzzles("user1"))
