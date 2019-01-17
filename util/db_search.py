import sqlite3 #imports sqlite

def getAllPuzzles():
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzle_content FROM puzzles;"
    c.execute(command)
    tList = c.fetchall()
    fList = []
    for element in tList:
        fList.append(str(element[0]))
    db.commit()
    db.close()
    return(fList)

print(getAllPuzzles())


def getMovesUser(username):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT moves FROM usersInfo WHERE usersInfo.username ='" + username + "';" #selects score of the user
    c.execute(command)
    oldScore = c.fetchone()[0]
    db.commit()
    db.close()
    return(oldScore)

'''
getPuzzlePlayedUser(username)
For any given username, it will return the number of puzzles that the user has played.
'''
def getPuzzlePlayedUser(username):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM logs WHERE logs.username ='" + username + "';" #selects score of the user
    c.execute(command)
    numPuzzlesDone = len(c.fetchall())
    return(numPuzzlesDone)

'''
getLikedPuzzles(username)
For any given username, it will return the puzzles that the user has saved.
'''
def getLikedPuzzles(username):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT likedPuzzles FROM usersInfo WHERE usersInfo.username ='" + username + "';" #selects score of the user
    c.execute(command)
    list  = c.fetchall()
    #print(list[0])
    db.commit()
    db.close()
    return (list[0][0])
    #return ("finished getlikedpuzzles")
#print(getLikedPuzzles("user1"))

'''
getPuzzleContent(puzzleID)
For any given puzzleID, it will return the description associated with it.
'''
def getPuzzleContent(puzzleID):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = 'SELECT puzzle_content from puzzles WHERE puzzles.puzzleID = (?)'
    c.execute(command, (puzzleID,))
    puzzle = str(c.fetchall()[0][0]) #retrieves the scores in descending order
    db.commit()
    db.close()
    #scores.sort(reverse=True)
    #return scores[0:5]
    return (puzzle)

'''
getPuzzleID(puzzle_description)
For any given puzzle description, it will return the ID associated with it.
'''
def getPuzzleID(puzzle_description):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM puzzles WHERE puzzles.puzzle_content ='" + str(puzzle_description) + "';" #selects score of the user
    c.execute(command)
    puzzle = str(c.fetchall()[0][0]) #retrieves the scores in descending order
    db.commit()
    db.close()
    return (puzzle)

'''
getMovesPuzzle(puzzleID)
For any given puzzle, it will return the average number of moves it takes for a given puzzle to be completed based off of logs.
'''
def getMovesPuzzle(puzzleID):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT averageMoves FROM puzzles WHERE puzzles.puzzleID ='" + str(puzzleID) + "';" #selects score of the user
    c.execute(command)
    oldScore = c.fetchone()[0]
    db.commit()
    db.close()
    return(oldScore)

'''
highScores(puzzleID)
For any given puzzle, it will return the highest scores (required the smallest number of moves to complete).
'''
def highScores(puzzleID):
    DB_FILE="data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    # command = "SELECT score, username from users"
    command = "SELECT moves FROM logs WHERE logs.puzzleID ='" + str(puzzleID) + "';" #selects score of the user
    c.execute(command)
    try:
        scores = c.fetchall() #retrieves the scores in descending order
        scores.sort(reverse=True)
        return scores[0]

    except:
        return 0

'''
getPuzzlePlayedPuzzle(puzzleID)
Returns the number of times a puzzle, with a specific ID, was played.
'''
def getPuzzlePlayedPuzzle(puzzleID):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM logs WHERE logs.puzzleID ='" + str(puzzleID)+ "';" #selects score of the user
    c.execute(command)
    numPuzzlesDone = len(c.fetchall())
    db.commit()
    db.close()
    return(numPuzzlesDone)

'''
password(username)
returns the password that matches the username if one exists
else return none
'''
def password(username):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    get_password = 'SELECT password FROM usersInfo WHERE usersInfo.username = (?)'
    c.execute(get_password,(username,))
    password = c.fetchone()
    return password

'''
username(username)
returns an empty list if username doesn't exist in the ./database
returns [username] if username exists
'''
def username(username):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    user_exists = 'SELECT username FROM usersInfo WHERE usersInfo.username = (?);'
    c.execute(user_exists,(username,))
    userList = c.fetchall()
    return userList
