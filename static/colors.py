import random

def puzzleGen(rows,cols):
    puzzle = []
    for r in range(rows):
        puzzle.append([])
        for c in range(cols):
            puzzle[r].append([])
    # puzzle[0][0] = [255,0,0]
    # puzzle[0][cols - 1] = [0,255,0]
    # puzzle[rows - 1][0] = [0,0,255]
    # for r in range(rows):
    #     puzzle[r][0] = [255 - r * 255.0/(rows - 1),0,0 + r * 255.0/(rows - 1)]
    # print(puzzle)
    # for r in range(rows):
    #     for c in range(cols):
    #         if len(puzzle[r][c]) != 3:
    #             puzzle[r][c] = [puzzle[r][0][0] ]
    for r in range(rows):
        for c in range(cols):
            puzzle[r][c] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return puzzle
