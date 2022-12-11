import time

from heuristic import heuristic
from boardtree import boardtree

class solve:
    def __init__(self, super):
        self.super = super

    def setAlgorithm(self, alg):
        """sets the used heuristic algorithm"""
        self.alg = alg
    
    def useAlgotithm(self, board1, board2):
        if(self.alg == "hemming"):
            return heuristic.hemming(board1, board2)
        elif(self.alg == "manhatten"):
            return heuristic.manhatten(board1, board2)
        else:
            self.super.killProg()

    def setMaxTime(self, duration):
        self.maxTime = duration

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
                    #dist = heuristic.hemming(i, goalboard)  #calculate distances
                    dist = self.useAlgotithm(i, goalboard)
                    if(dist == 0):
                        stop = True
                        #self.super.printBoard(i)
                        timeNeeded = time.time() - startTime
                        print("found in " + str(iterations+1)  + " iterations and " + str(timeNeeded) + "sec using " + str(self.alg))
                    if(not self.boardtree.checkBoardExists(i)):
                        self.boardtree.addBoard(i, dist, False) #store nodes

            self.boardtree.setExpanded(board)   #set expanded to parent board
            
            if(time.time() > startTime + self.maxTime):
                stop = True
                print("no solution found in time using " + str(self.alg))