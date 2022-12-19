import sys
import random

from solve import solve
from store import store

class puzzle:
    """
    inlcudes the main parts of 8-puzzle.

    ...

    Attributes
    ----------
    filelocation : str
        path to the performance.txt file in order to store resulting data.

    Methods
    -------
    killProg():
        kills the program
    printBoard(board):
        prints the given board
    logic():
        is responsible for the logic of this program
    """

    def __init__(self, filelocation):
        """
        initializes the puzzle object
        
        Parameters:
            self (puzzle): puzzle object.
            filelocation (String): path to the performance.txt file in order to store resulting data.

        Returns:
            -
        """
        self.startboard = []
        self.goalboard = []
        self.datafilelocation = filelocation

    def killProg(self):
        """
        kills the program
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            -
        """
        sys.exit()
        
    def __inputOrder(self):
        """
        is used by __userInput() to read the 3x3 matrix
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            field (Array): 3x3 array with the read values
        """
        field = []
        for i in range(0,3):
            temp = input().split(" ")
            field.append(temp)
        return field

    def __userInput(self):
        """
        reads the user input of startboard and the goalboard
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            -
        """
        print("Enter start order")
        self.startboard = self.__inputOrder()
        print("Enter goal order")
        self.goalboard = self.__inputOrder()

    def __verifyGameboardSizeEqual(self):
        """
        verifys that startboard has the same size as goalboard
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            -
        """
        raise NotImplementedError

    def printBoard(self, board):
        """
        prints the given board
        
        Parameters:
            self (puzzle): puzzle object.
            board (Array): board that has to be printed

        Returns:
            -
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j] + " ", end="")
            print()
        print("------------------")

    def __setStartboard(self):
        """
        sets the startboard thus no inputs has to be made every time during testing phase
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            -
        """
        #board = [["1", "2", "3"],
        #         ["4", "8", "5"],
        #         ["_", "7", "6"]]
        #board = [["8", "1", "2"],
        #         ["_", "4", "3"],
        #         ["7", "6", "5"]]
        board = [["8", "1", "4"],
                 ["5", "7", "3"],
                 ["2", "6", "_"]]
        self.startboard = board

    def __createRandomStartboard(self):
        """
        this method generates a random startboard and stores it in self.startboard
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            -
        """
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
        """
        sets the goalboard thus no inputs has to be made every time during testing phase
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            -
        """
        #board = [["1", "2", "3"],
        #         ["4", "5", "6"],
        #         ["7", "8", "_"]]
        board = [["_", "1", "2"],
                 ["3", "4", "5"],
                 ["6", "7", "8"]]
        self.goalboard = board

    def logic(self):
        """
        is responsible for the logic of this program
        
        Parameters:
            self (puzzle): puzzle object.

        Returns:
            -
        """
        #self.__userInput()
        #self.__setStartboard()
        self.__setGoalboard()

        self.solve = solve(self)
        self.solve.setMaxTime(5)

        for i in range(500):
            self.__createRandomStartboard()
            if(self.solve.isSolvable(self.startboard)):
                print("solvable")
                self.solve.setAlgorithm("hamming")
                [alg1, iterations1, timeNeeded1] = self.solve.solvepuzzle(self.startboard, self.goalboard)
                self.solve.setAlgorithm("manhatten")
                [alg2, iterations2, timeNeeded2] = self.solve.solvepuzzle(self.startboard, self.goalboard)
                
                data = str(iterations1) + "\t" + str(timeNeeded1) + "\t" + str(iterations2) + "\t" + str(timeNeeded2) + "\n"
                store.writeToTxt(self.datafilelocation, data)
                print("----------------------------------------")
            else:
                print("not solvable")
                self.printBoard(self.startboard)

if __name__ == "__main__":
    datalocation = "Code/performance.txt"
    game = puzzle(datalocation)
    game.logic()