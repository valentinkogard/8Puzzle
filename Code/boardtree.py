import copy

class boardtree:

    def __init__(self):
        """initializes the puzzle object"""
        self.board = []

    def addBoard(self, board, distance, expanded):
        """adds a new board to the board list"""
        self.board.append({
            "board": board,
            "distance": distance,
            "expanded" : expanded
        })

    def __findEmptyField(self, board):
        """finds the empty field on the given board"""
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == "_"):
                    return i, j

    def __switch(self, board, x1, y1, x2, y2):
        """switches the icons of (x1,y1) and ((x2,y2)"""
        newboard = copy.deepcopy(board)
        try:
            symbol1 = newboard[x1][y1]
            symbol2 = newboard[x2][y2]
            newboard[x1][y1] = symbol2
            newboard[x2][y2] = symbol1
            return newboard
        except IndexError:
            return None

    def createChildren(self, board):
        """creates all possible child boards from a given board"""
        val = []
        row, col = self.__findEmptyField(board["board"])
        list = [[row, col+1], [row+1, col], [row, col-1], [row-1, col]]
        for i in range(len(list)):
            val.append(self.__switch(board["board"], row, col, list[i][0], list[i][1]))
        return val            

    def compare(self, board1, board2):
        "compare two boards - if they are the same return true otherwise return false"
        for i in range(len(board1)):
            for j in range(len(board1[0])):
                if(not board1[i][j] == board2[i][j]):
                    return False
        return True

    def setExpanded(self, board):
        """sets the expanded tag to true for a given board"""
        for i in self.board:
            if(i["expanded"] == False and self.compare(i["board"], board["board"])):
                i["expanded"] = True
                return

    def checkBoardExists(self, board):
        """check whether board already exists or not - if it exists return true otherwise false"""
        for i in self.board:
            if(self.compare(i["board"], board)):
                return True
        return False

    def getAllBoards(self):
        """returns all stored boards"""
        return self.board
    
    def getNumOfAllBoards(self):
        """returns the total number of boards stored"""
        return len(self.getAllBoards)

    def getBoardWithLowestDist(self):
        """returns the board with the lowest ditsance to solution which is at this point not jet expanded"""
        board = None
        dist = 1000000

        for i in self.board:
            if(i["distance"] < dist and i["expanded"] == False):
                board = i
                dist = i["distance"]
        return board
        