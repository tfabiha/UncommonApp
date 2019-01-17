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

def getPuzzlePlayedUser(username):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT puzzleID FROM logs WHERE logs.username ='" + username + "';" #selects score of the user
    c.execute(command)
    numPuzzlesDone = len(c.fetchall())
    return(numPuzzlesDone)

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
#print (getPuzzle(1))

def getPuzzleID(puzzle_description):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = 'SELECT puzzleID from puzzles WHERE puzzles.puzzle_content = (?)'
    c.execute(command, (puzzle_description,))
    puzzle = str(c.fetchall()[0][0]) #retrieves the scores in descending order
    db.commit()
    db.close()
    #scores.sort(reverse=True)
    #return scores[0:5]
    return (puzzle)

print("GET PUZZLEID")
print(getPuzzleID("apuzzle1"))

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
highScores(puzzleID)
For any given puzzle, it will return the top ten users and their moves
Returns the top 10 in descending order
'''

def puzzleHighScores(puzzleID):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = 'SELECT username, moves from logs WHERE logs.puzzleID = (?)'
    c.execute(command, (puzzleID,))
    scores = c.fetchall() #retrieves the scores in descending order
    print(scores)
    scores.sort(reverse=True)
    return scores[0:5]

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

'''
score(username)
retrieves score of user
'''
def score(username):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    user_exists = 'SELECT score FROM users WHERE users.username = (?);'
    c.execute(user_exists,(username,))
    score = c.fetchone()
    return score

'''
question(username,question)
returns question if user already answered that question
None if user didn't answer
'''

def question(username,question):
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()
    command = 'SELECT question FROM questions WHERE questions.username = (?) AND questions.question = (?);'
    c.execute(command, (username, question))
    match = c.fetchone()
    return match
