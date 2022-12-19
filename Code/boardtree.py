import copy

class boardtree:
    """
    A class that includes all created boards.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    addBoard(board, distance, expanded):
        adds a new board to the board list
    createChildren(board):
        creates all possible child boards from a given board
    compare(board1, board2):
        compare two boards - if they are the same return true otherwise return false
    setExpanded(board):
        sets the expanded tag to true for a given board
    checkBoardExists(board):
        check whether board already exists or not - if it exists return true otherwise false
    getAllBoards():
        returns all stored boards
    getNumOfAllBoards():
        returns the total number of boards stored
    getBoardWithLowestDist():
        returns the board with the lowest ditsance to solution which is at this point not jet expanded
    """

    def __init__(self):
        """
        initializes the puzzle object
        
        Parameters:
            self (boardtree): boardtree object.

        Returns:
            -
        """
        self.board = []

    def addBoard(self, board, distance, expanded):
        """
        adds a new board to the board list
        
        Parameters:
            self (boardtree): boardtree object.
            board (Array): a 2D matix.
            distance (Int): heuristic distance
            expanded (Bool): if the board has children -> false; otherwise -> true

        Returns:
            -
        """
        self.board.append({
            "board": board,
            "distance": distance,
            "expanded" : expanded
        })

    def __findEmptyField(self, board):
        """
        finds the empty field on the given board
        
        Paramters:
            self (boardtree): boardtree object.
            board (Array): a 2D matix.

        Returns:
            i (Int): row of space
            j (Int): column of space
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == "_"):
                    return i, j

    def __switch(self, board, x1, y1, x2, y2):
        """
        switches the icons of (x1,y1) and ((x2,y2)
        
        Paramters:
            self (boardtree): boardtree object.
            board (Array): a 2D matix.
            x1 (Int): first icon row
            y1 (Int): first icon column
            x2 (Int): second icon row
            y2 (Int): seconf icon clomun

        Returns:
            newboard (Array): row of space
        """
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
        """
        creates all possible child boards from a given board
        
        Parameters:
            self (boardtree): boardtree object.
            board (Array): a 2D matix.

        Returns:
            val (Array): list of boards with all possible next moves
        """
        val = []
        row, col = self.__findEmptyField(board["board"])
        list = [[row, col+1], [row+1, col], [row, col-1], [row-1, col]]
        for i in range(len(list)):
            val.append(self.__switch(board["board"], row, col, list[i][0], list[i][1]))
        return val            

    def compare(self, board1, board2):
        """
        compare two boards - if they are the same return true otherwise return false
        
        Parameters:
            self (boardtree): boardtree object.
            board1 (Array): a 2D matix.
            board2 (Array): a 2D matix.   

        Returns:
            same (Bool): true if board1 is equal to board2; otherwise false
        """
        for i in range(len(board1)):
            for j in range(len(board1[0])):
                if(not board1[i][j] == board2[i][j]):
                    return False
        return True

    def setExpanded(self, board):
        """
        sets the expanded tag to true for a given board
        
        Parameters:
            self (boardtree): boardtree object.
            board (Array): a 2D matix.

        Returns:
            -      
        """
        for i in self.board:
            if(i["expanded"] == False and self.compare(i["board"], board["board"])):
                i["expanded"] = True
                return

    def checkBoardExists(self, board):
        """
        check whether board already exists or not - if it exists return true otherwise false
        
        Parameters:
            self (boardtree): boardtree object.
            board (Array): a 2D matix.

        Returns:
            exists (Bool): true if board exists; otherwise false     
        """
        for i in self.board:
            if(self.compare(i["board"], board)):
                return True
        return False

    def getAllBoards(self):
        """
        returns all stored boards
        
        Parameters:
            self (boardtree): boardtree object.

        Returns:
            board (Array): a 2D matix (board).     
        """
        return self.board
    
    def getNumOfAllBoards(self):
        """
        returns the total number of boards stored
        
        Parameters:
            self (boardtree): boardtree object.

        Returns:
            length (Int): total length of all boards created 
        """
        return len(self.getAllBoards)

    def getBoardWithLowestDist(self):
        """
        returns the board with the lowest ditsance to solution which is at this point not jet expanded
        
        Parameters:
            self (boardtree): boardtree object.

        Returns:
            board (Array): a 2D marix.     
        """
        board = None
        dist = 1000000

        for i in self.board:
            if(i["distance"] < dist and i["expanded"] == False):
                board = i
                dist = i["distance"]
        return board
        