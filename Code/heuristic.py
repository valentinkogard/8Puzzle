

class heuristic:

    def hemming(board1, board2):
        """
        heuristic function which counts wrong placed fields.
  
        Parameters:
            board1 (Array): a 2D matrix.
            board2 (Array): a 2D matrix.
          
        Returns:
            counter (int): number of missmatches.
        """
        counter = 0

        for i in range(len(board1)):
            for j in range(len(board1[0])):
                if(board1[i][j] != board2[i][j]):
                    counter += 1
        return counter

    def __calcDistManhatten(board1, board2, row, col):
        """calculates the manhatten distance between should place and current place"""
        symbol = board1[row][col]

        for i in range(len(board1)):
            for j in range(len(board1[0])):
                if(symbol == board2[i][j]):
                    horizontalDist = abs(row - i)
                    verticalDist = abs(col - j)
                    return horizontalDist + verticalDist

    def manhatten(board1, board2):
        "distance between solution and start point"
        distance = 0

        for i in range(len(board1)):
            for j in range(len(board1[0])):
                distance += heuristic.__calcDistManhatten(board1, board2, i, j)
        return distance

