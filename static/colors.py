import random

def puzzleGen(rows,cols,URC,ULC,LRC,LLC):
    puzzle = []

    for r in range(rows):
        puzzle.append([])

        for c in range(cols):
            puzzle[r].append([])
    topHorVar = [(URC[0] - ULC[0])/(rows - 1),(URC[1] - ULC[1])/(rows - 1),(URC[2] - ULC[2])/(rows - 1)]
    print(topHorVar)
    botHorVar = [(LRC[0] - LLC[0])/(rows - 1),(LRC[1] - LLC[1])/(rows - 1),(LRC[2] - LLC[2])/(rows - 1)]
    leftVerVar = [(ULC[0] - LLC[0])/(rows - 1),(ULC[1] - LLC[1])/(rows - 1),(ULC[2] - LLC[2])/(rows - 1)]
    rightVerVar = [(URC[0] - LRC[0])/(rows - 1),(URC[1] - LRC[1])/(rows - 1),(URC[2] - LRC[2])/(rows - 1)]
    for c in range(cols):
        puzzle[0][c] = [URC[0] + c * topHorVar[0],URC[1] + c * topHorVar[1],URC[2] + c * topHorVar[2]]
        print(puzzle[0][c])
    return puzzle
