# UncommonApp
# Dennis Chen, T Fabiha, Addison Huang, Michelle Tang
P #02: The End

## Project Description
Using RESTful APIs we will mimic the game “i love hue.” People will be given a color scheme that broken is into pieces then randomized. Certain pieces will be locked, which will serve as a point of reference for people to complete the puzzle. They will then have to reorganize the pieces until the original color scheme is achieved. Creating an account will also allow users to create their own puzzles with customizations such as the size of the puzzle and the color scheme. Based off of a player’s location and weather, players will be able to play limited edition puzzles. There will be puzzles that we (the devs) created that are open to everyone. For all puzzles, there will be a tracker to count how many moves are made per puzzle, which is then compared to the ‘world’ average. 

## APIs
**Here are the APIs that we use & how to procure keys:**

API Name | Link | Key & Quota | How to Create Key 
--- | --- | --- | ---
COLOURlovers API | TBD  | no key needed and unlimited quotas! | N/A
IP Identifier | http://ip-api.com | no key needed and unlimited quotas! | Create an account and on the dashboard where it says API key, follow those instructions.
Weather API | TBD | no key needed and unlimited quotas! | N/A

** Where to place your API **
1) Please put your API key in a file named ```keys.json``` with a key value of weather. 

## Instructions to Run:

1. Check to see if you have python3 installed by running ``` python3 ``` in the terminal. It should produce something like: 
```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
2. Install python3-venv and create your own environment by running the following in terminal. Replace <VENV> with the name of your virtual environment (your choice).
```
$ sudo apt install python3-venv
$ python3 -m venv <VENV>
```
3. Activate the virtual environment by typing ```$ . PATH_TO_VENV/bin/activate``` in the terminal. Make sure you are in the directory which contains the virtual environment. To check, type in ```ls``` to get a current listing of the files in your current working directory.  

4. Install the dependencies with [requirements.txt](requirements.txt) by running the following command  

    ```
    pip install -r requirements.txt
    ```
  
5. Clone this repo by typing ```$ git clone git@github.com:tfabiha/UncommonApp.git``` in the terminal. 

6. Change into the repo (```cd UncommonApp```)and run the python file by typing ```$ python app.py``` in the terminal. 
7. If successful, the following message will appear in the terminal:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 248-748-502
```
  
Flask: Runs the web application on local host.
Wheel: Used for Flask.
SQLite: Creates databases for storing information.
URLLib3: Receives information from APIs.

 ## Dependencies: 
1. Flask: Runs the web application on local host.
2. Wheel: Used for Flask.
3. SQLite: Creates databases for storing information.
4. URLLib3: Receives information from APIs.
5. passlib: Provides a hash password (keeps you safe!)
