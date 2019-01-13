import sqlite3 #imports sqlite

def users(): #creates the users db
    DB_FILE="./data/userInfo.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE users(username TEXT, password TEXT, moves INTEGER, likedPuzzles TEXT)"
    c.execute(command)

def questions(): #creates the puzzles db
    DB_FILE="./data/puzzles.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE puzzles(puzzleID INTEGER, puzzle_content TEXT, averageMoves INT)"
    c.execute(command)

def logs(): #creates the logs db
    DB_FILE="./data/logs.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE logs(username TEXT, moves INTEGER, puzzleID INTEGER)"
    c.execute(command)

def main(): #calls all of the functions to build the databases
    try:
        users()
        questions()
        logs()

    except:
        pass

main()
print("finished creating all of the databases")
