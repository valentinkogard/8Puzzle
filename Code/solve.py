import time
import math

from heuristic import heuristic
from boardtree import boardtree

class solve:
    def __init__(self, super):
        """initializes the puzzle object"""
        self.super = super

    def setAlgorithm(self, alg):
        """sets the used heuristic algorithm"""
        self.alg = alg
    
    def useAlgotithm(self, board1, board2):
        """is used to switch between different heuristic functions / used in combination with setAlgorithm()"""
        if(self.alg == "hemming"):
            return heuristic.hemming(board1, board2)
        elif(self.alg == "manhatten"):
            return heuristic.manhatten(board1, board2)
        else:
            self.super.killProg()

    def setMaxTime(self, duration):
        """set the max duration for a single solvepuzzle board / if time exceeded attempt"""
        self.maxTime = duration

    def isSolvable(self, board):
        """counts the inversions - if inversion is odd the puzzle is NOT solveable / if the inversion is even the puzzle is solveable"""
        counter = 0

        for i in range(len(board)*len(board[0])-1):
            row1 = math.floor(i/len(board))
            col1 = i % len(board)
            for j in range(i+1, len(board)*len(board[0])):
                row2 = math.floor(j/len(board))
                col2 = j % len(board)
                if(board[row1][col1] != "_" and board[row2][col2] != "_"):
                    if(int(board[row1][col1]) > int(board[row2][col2])):
                        counter += 1
        if(counter % 2 == 0):
            return True
        return False

    def solvepuzzle(self, startboard, goalboard):
        stop = False
        iterations = 0
        startTime = time.time()

        self.boardtree = boardtree()
        self.boardtree.addBoard(startboard, self.useAlgotithm(startboard, goalboard), False)

        while(not stop): 
            iterations += 1
            board = self.boardtree.getBoardWithLowestDist() #get board with lowest distance
            #self.super.printBoard(board["board"])
            newBoards = self.boardtree.createChildren(board)    #create children
            
            for i in newBoards:
                if(i != None):
                    dist = self.useAlgotithm(i, goalboard)  #calculate distances
                    if(dist == 0 and self.boardtree.compare(i, goalboard)):
                        stop = True
                        #self.super.printBoard(i)
                        timeNeeded = time.time() - startTime
                        print("found in " + str(iterations+1)  + " iterations and " + str(timeNeeded) + "sec using " + str(self.alg))
                        return self.alg, iterations+1, timeNeeded
                    if(not self.boardtree.checkBoardExists(i)):
                        self.boardtree.addBoard(i, dist, False) #store nodes

            self.boardtree.setExpanded(board)   #set expanded to parent board
            
            if(time.time() > startTime + self.maxTime):
                stop = True
                print("no solution found in time using " + str(self.alg))
                return self.alg, 0, self.maxTime