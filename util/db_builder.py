import sqlite3 #imports sqlite

'''
users()
creates a table in the uncommonApp.db named usersInfo
'''
def users(): #creates the users db
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE usersInfo(username TEXT PRIMARY KEY, password TEXT, moves INTEGER, likedPuzzles TEXT)"
    c.execute(command)

'''
puzzles()
creates a table in the uncommonApp.db named puzzles
'''
def puzzles(): #creates the puzzles db
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE puzzles(puzzleID INTEGER PRIMARY KEY AUTOINCREMENT, puzzle_content TEXT, averageMoves INT)"
    c.execute(command)

'''
logs()
creates a table in the uncommonApp.db named logs
'''
def logs(): #creates the logs db
    DB_FILE="./data/uncommonApp.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor() #facilitates db operations
    command = "CREATE TABLE logs(username TEXT, moves INTEGER, puzzleID INTEGER)"
    c.execute(command)

def main(): #calls all of the functions to build the databases
    try:
        print("sm")
        users()
        puzzles()
        logs()
        print("what")
    except:
        pass

main()
print("databases created")
