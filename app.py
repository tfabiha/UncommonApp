from flask import Flask,render_template,request,session,url_for,redirect,flash

from os import urandom
from util import db_updater as update
from util import db_search as search
from util import db_builder as builder
from util import colors
from util import weatherColors
from passlib.hash import sha256_crypt

import ssl
import urllib
import json
import random

import sqlite3 #imports sqlite

app = Flask(__name__)
app.secret_key = urandom(32)

#----------------------------------------------------------home--------------------------------------------------------
@app.route("/",methods=['GET','POST'])
def home():
    builder.main()
    if 'username' in session: #if user is logged in
        return redirect(url_for('authPage'))
    else:
        return render_template('auth.html')

#----------------------------------------------------------login/register/logout--------------------------------------------------------
@app.route("/logout")
def logout():
    '''
    Logs user out of session by popping them from the session. Returns user to log-in screen
    '''
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('authPage'))
    else:
        return redirect(url_for('home'))

@app.route("/auth",methods=['GET','POST'])
def authPage():
    '''
    Authenticates user signing in. Checks to see if password is correct or not;
    if correct, logs user in. If not, flashes "incorrect credentials"
    '''
    if 'username' in session:
        username = session['username']
        '''score = search.score(username)[0]
        scores = search.highScores()
        counter = 0
        highScores = []
        userNames = []

        while counter < len(scores):
            highScores.append(scores[counter][0])
            userNames.append(scores[counter][1])
            counter += 1
'''
        return redirect(url_for('genWeather'))
    else:
        try:
            username=request.form['username'] #username
            password = search.password(username) #password that matches the username
            print(password)
            if password == None: #if credentials are incorrect
                flash('Wrong Username or Password!')
                return redirect(url_for('home')) #redirects
            elif sha256_crypt.verify(request.form['password'], password[0]): #if password is correct, login
                session['username'] = username
                return redirect(url_for('authPage'))
            else: #else credentials are wrong
                flash('Wrong Username or Password!')
                return redirect(url_for('home'))
        except:
            return redirect(url_for('home'))

@app.route("/reg",methods=['GET','POST'])
def reg():
    '''
    Loads the template that takes information and allows user to register,
    creating a new account that they can sign into session with
    '''
    if 'username' in session:
        return redirect(url_for('authPage'))

    return render_template('reg.html')

#----------------------------------------------------------database--------------------------------------------------------
@app.route("/added",methods=['GET','POST'])
def added():
    '''
    Checks to see if username is unique,
    flashes "username taken" if it is,
    adds user and password to database if not and sends to home
    '''
    try:
        if request.form['password'] == request.form['confirmpassword']:
            newUsername = request.form['username']
            newPassword = sha256_crypt.encrypt(request.form['password']) #encrypts password
            userList = search.username(newUsername)
            if userList == [] : #if username isn't taken
                update.adduser(newUsername,newPassword) #add to database
                flash('Register Successful')
                return redirect(url_for('home'))
            else: #if username is taken
                flash('Username Taken')
                return redirect(url_for('reg'))
        else:
            flash("Passwords don't match")
            return redirect(url_for('reg'))
    except:
        return redirect(url_for('home'))

#-------------------------------------------featured puzzle--------------------------------------------------------
@app.route('/weatherPuz',methods = ['GET','POST'])
def genWeather():
    '''
    Generates a featured puzzle based on the current weather of the user and puts
    it on the home page
    '''
    if 'username' not in session:
        redirect(url_for('authPage'))
    else:
        name = session['username']
        rows = 8
        columns = 8
        palette = weatherColors.makePuzOnWeather()
        puzzle = colors.puzzleGen(rows,columns,palette[0],palette[1],palette[2],palette[3])
        return render_template('home.html',
                               Name = name,
                               colors = puzzle,
                               tile_size = "{}x{}".format(rows, columns), # size "widthxheigth"
                               UL = "{},{},{}".format(palette[0][0],
                                                      palette[0][1],
                                                      palette[0][2]), # upper-left color
                               UR = "{},{},{}".format(palette[1][0],
                                                      palette[1][1],
                                                      palette[1][2]), # upper-right color
                               LL = "{},{},{}".format(palette[2][0],
                                                      palette[2][1],
                                                      palette[2][2]), # lower-left color
                               LR = "{},{},{}".format(palette[3][0],
                                                      palette[3][1],
                                                      palette[3][2])) # lower-right color
#-------------------------------------------create puzzle--------------------------------------------------------
@app.route('/create',methods = ['GET','POST'])
def create():
    rows = 8
    columns = 8

    palette = colors.getpalette(4)
    puzzle = colors.puzzleGen(rows, columns,
                              palette[0], palette[1],
                              palette[2], palette[3])

    return render_template('testpuzzle.html',
                           colors = puzzle,
                           tile_size = "{}x{}".format(rows, columns), # size "widthxheigth"
                           UL = "{},{},{}".format(palette[0][0],
                                                  palette[0][1],
                                                  palette[0][2]), # upper-left color
                           UR = "{},{},{}".format(palette[1][0],
                                                  palette[1][1],
                                                  palette[1][2]), # upper-right color
                           LL = "{},{},{}".format(palette[2][0],
                                                  palette[2][1],
                                                  palette[2][2]), # lower-left color
                           LR = "{},{},{}".format(palette[3][0],
                                                  palette[3][1],
                                                  palette[3][2])) # lower-right color

if __name__ == '__main__':
    app.run(debug=True)
