import sys
import random

from solve import solve

class puzzle:
    def __init__(self):
        self.startboard = []
        self.goalboard = []

    def killProg():
        sys.exit()
        
    def __inputOrder(self):
        """is used by __userInput() to read the 3x3 matrix"""
        field = []
        for i in range(0,3):
            temp = input().split(" ")
            field.append(temp)
        return field

    def __userInput(self):
        """reads the user input of startboard and the goalboard"""
        print("Enter start order")
        self.startboard = self.__inputOrder()
        print("Enter goal order")
        self.goalboard = self.__inputOrder()

    def __verifyGameboardSizeEqual(self):
        """verifys that startboard has the same size as goalboard"""
        pass

    def printBoard(self, board):
        """prints the given board"""
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j] + " ", end="")
            print()
        print("------------------")

    def __setStartboard(self):
        """sets the startboard thus no inputs has to be made every time during testing phase"""
        board = [["1", "2", "3"],
                 ["4", "8", "5"],
                 ["_", "7", "6"]]
        self.startboard = board

    def __createRandomStartboard(self):
        items = ["1", "2", "3", "4", "5", "6", "7", "8", "_"]
        random.shuffle(items)
        counter = 0
        randboard = [["", "", ""],["", "", ""],["", "", ""]]

        for i in range(3):
            for j in range(3):
                randboard[i][j] = items[counter]
                counter += 1
        self.startboard = randboard

    def __setGoalboard(self):
        """sets the goalboard thus no inputs has to be made every time during testing phase"""
        board = [["1", "2", "3"],
                 ["4", "5", "6"],
                 ["7", "8", "_"]]
        self.goalboard = board

    def logic(self):
        """is responsible for the logic of this program"""
        
        #self.__userInput()
        self.__setStartboard()
        self.__setGoalboard()

        self.solve = solve(self)
        self.solve.setMaxTime(5)

        for i in range(100):
            self.__createRandomStartboard()
            self.solve.setAlgorithm("hemming")
            self.solve.solvepuzzle(self.startboard, self.goalboard)
            self.solve.setAlgorithm("manhatten")
            self.solve.solvepuzzle(self.startboard, self.goalboard)
            print("----------------------------------------")

if __name__ == "__main__":
    game = puzzle()
    game.logic()