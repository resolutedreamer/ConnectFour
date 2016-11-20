#!/usr/bin/env python

class ConnectFour():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = []
        self.columnCounts = [0]*width
        for i in range(width):
            self.board.append([0]*height)
        
        # False while game is being played; True when a player wins
        self.gameOver = False
        # True for player 1, False for player 2
        self.currentPlayer = True
        

    def getPlayerNum(self):
        if self.currentPlayer == True:
            return '1'
        if self.currentPlayer == False:
            return '2'

    def print_board(self):
        for cidx, column in enumerate(self.board):
            for ridx, row in enumerate(column):
                print self.board[cidx][ridx],
            print

    def play(self):
        while not self.gameOver:
            self.print_board()

            print "Player" + self.getPlayerNum() + "'s Turn"
            performedMove = self.getPlayerMove()
            self.checkVictory(performedMove)
            if(self.gameOver):
                print "Player " + self.currentPlayer + " wins!"
            else:
                self.currentPlayer = not self.currentPlayer


    def getPlayerMove(self):
        validMove = False
        column = -1
        while not validMove:
            column_str = raw_input("Please select a column: ")
            if column_str.isdigit():
                column_int = int(column)
                validMove = self.checkValidMove(column_int)
        return self.performPlayerMove(column_int)

    def checkValidMove(self, column):
        if column >=0 and column < self.width:
            #column is in the width of the board
            if self.columnCounts[column] < self.height:                    
                #column is not already filled
                return True
            else:
                print "Column full"
        return False
        
    def performPlayerMove(self, column):
        nextEmptySpace = self.columnCounts[column]
        playerToken = self.getToken()
        print "Performing Move"
        curCol = self.board[column]
        curCol[nextEmptySpace] = playerToken
        self.columnCounts[column] += 1
        return (column, nextEmptySpace)

    def checkMatch(self, x, y, playerToken, inARow = 0):
        # Recursively checks to see if there are 4 of playerToken in a row
        if inARow == 4:
            # There are 4 in a row
            return True
        elif x <= 0 or x >= self.width - 1:
            # Cannot look past the left or right edge of the board
            return False
        #check left
        if (self.board[x-1][y] == playerToken):
            #keep searching left
            self.checkMatch(x-1, y, playerToken, inARow + 1)
        #check right
        if(self.board[x+1][y] == playerToken):
            #keep searching right
            self.checkMatch(x+1, y, playerToken, inARow + 1)
        
        if y == 0:
            # This is the bottom of a column, can't look below the bottom
            return False        
        
        #check below
        elif(self.board[x][y-1] == playerToken, inARow):
            #keep searching down
            self.checkMatch(x, y-1, playerToken, inARow + 1)
        #check belowleft
        elif(self.board[x-1][y-1] == playerToken, inARow):
            #keep searching belowleft
            self.checkMatch(x-1, y-1, playerToken, inARow + 1)
        #check belowright
        elif(self.board[x+1][y-1] == playerToken, inARow):
            #keep searching belowright
            self.checkMatch(x+1, y-1, playerToken, inARow + 1)
        else:
            #there was no further match to the left, right, below, belowleft, or belowright
            return False
        

    def getToken(self):
        if self.currentPlayer:
            playerToken = 1
        else:
            playerToken = -1
        return playerToken
    
    def checkVictory(self, currentMove):
        playerToken = self.getToken()
        column = currentMove[0]
        row = currentMove[1]
        if self.checkMatch(column, row, playerToken, 0):
            self.gameOver = True
        else:
            self.gameOver = False

def main():
    newGame = ConnectFour(8, 9)
    newGame.play()

if __name__ == '__main__':
    main()