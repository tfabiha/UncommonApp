import random
import json
from urllib import request, parse

'''
getpalette(count)
Parameters: count
Generates colors that will be used as the four corners in a puzzle after making a request from the API. The number of colors returned is based off of counts.
'''
def getpalette(count):
    p_all = []
    num_colors = 0

    while num_colors < count:
        URL_PALETTE = "http://www.colourlovers.com/api/palettes/random?format=json"

        response = request.Request(URL_PALETTE, headers =
                                   {"User-Agent": "Mozilla/5.0"})
        response = request.urlopen(response)
        response = response.read()

        palettes = json.loads(response)
        palettes = palettes[0]

        # print(palettes)
        palettes = palettes["colors"]

        num_colors = len(palettes)

    for i in range(count):
        color = palettes[i] # ffffff

        response = {}
        response["r"] = int( color[0:2] , 16 )
        response["g"] = int( color[2:4] , 16 )
        response["b"] = int( color[4:6] , 16 )

        #print(response)

        '''
        URL_COLOR = "http://www.thecolorapi.com/id?hex={}&format=json".format(color)

        response = request.urlopen(URL_COLOR)
        response = response.read()
        response = json.loads(response)

        # print(response)
        response = response["rgb"]
        '''

        data = [response["r"], response["g"], response["b"]]
        p_all.append( data )

    # print(palettes)
    # print(p_all)
    return p_all

# getpalette(4);
'''
puzzleGen(rows, cols, ULC, URC, LLC, LRC)
parameters: rows, cols, ULC, URC, LLC, LRC
Will create the basic outline for any given puzzle after the user supplies the number of rows, cols, and the four colorsself.
'''
def puzzleGen(rows, cols, ULC, URC, LLC, LRC):
    puzzle = []

    for r in range(rows):
        puzzle.append([])

        for c in range(cols):
            puzzle[r].append([])

    puzzle[0][0] = ULC
    puzzle[0][cols - 1] = URC
    puzzle[rows - 1][cols - 1] = LRC
    puzzle[rows - 1][0] = LLC


    """
    puzzle[0][0] = [random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255)]
    puzzle[0][cols - 1] = [random.randint(0,255),
                           random.randint(0,255),
                           random.randint(0,255)]
    puzzle[rows - 1][cols - 1] = [random.randint(0,255),
                                  random.randint(0,255),
                                  random.randint(0,255)]
    puzzle[rows - 1][0] = [random.randint(0,255),
                           random.randint(0,255),
                           random.randint(0,255)]
    """

    top_change = []
    bottom_change = []

    for i in range(3):
        top_change.append((puzzle[0][cols - 1][i] - puzzle[0][0][i]) / (cols - 1))
        bottom_change.append((puzzle[rows - 1][cols - 1][i] - puzzle[rows - 1][0][i]) / (cols - 1))

    for c in range(cols):
        if puzzle[0][c] == []:
            for i in range(3):
                puzzle[0][c].append(puzzle[0][0][i] + top_change[i] * c)

        if puzzle[rows - 1][c] == []:
            for i in range(3):
                puzzle[rows - 1][c].append(puzzle[rows - 1][0][i] + bottom_change[i] * c )

    for c in range(cols):
        change = []

        for i in range(3):
            change.append((puzzle[rows - 1][c][i] - puzzle[0][c][i]) / (rows - 1))

        for r in range(rows):
            if puzzle[r][c] == []:
                for i in range(3):
                    puzzle[r][c].append(int(puzzle[0][c][i]) + int(change[i] * r))

    return puzzle
