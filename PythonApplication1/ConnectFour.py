class ConnectFour():
    def __init__(self, height, width):
        self.board = []
        for i in range(width):
            self.board.append([0]*height)

        self.gameOver = False
        self.currentPlayerTurn = True
        # True for player 1, False for player 2
        while True:
            for i in range(len(self.board)):
                for j in range (len(self.board[0])):
                    print self.board[i][j],
                print

            print "Player" + str(self.currentPlayerTurn) + "'s Turn"
            previousMove = self.getPlayerMove(self.currentPlayerTurn)
            self.checkVictory(self.currentPlayerTurn, previousMove)
            if(self.gameOver == True):
                print "Player " + self.currentPlayerTurn + " wins!"
            else:
                self.currentPlayerTurn = not self.currentPlayerTurn


    def getPlayerMove(self, playerNumber):
        validMove = False
        column = 0
        while not validMove:
            column = int(raw_input("Which column would you like to place your token?"))
            print column            
            if column >=0 and column < len(self.board):
                #column is okay, can place the token
                validMove = True
        #column contains a valid column
        #actually perform the token insertion here
        return self.performPlayerMove(column, playerNumber)

    def performPlayerMove(self, column, playerNumber):
        playerToken = self.getToken(playerNumber)
        print "Performing Move"
        for idx, row in enumerate(self.board[column]):
            if idx == len(self.board[column])-1:
                self.board[column][idx] = playerToken
            print "row:"
            print row
            if row == 0:
                continue
            else:
                self.board[column][row-1] = playerToken
        return (column, row-1)        

    def checkMatch(self, x, y, playerToken, inARow = 0):
        # fix off by one errors here
        if inARow == 4:
            return True
        #check left
        if (self.board[x-1][y] == playerToken):
            #keep searching left
            self.checkMatch(x-1, y, playerToken, inARow + 1)
        #check right
        elif(self.board[x+1][y] == playerToken):
            #keep searching right
            self.checkMatch(x+1, y, playerToken, inARow + 1)
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
        

    def getToken(self, playerNumber):
        if playerNumber:
            playerToken = 1
        else:
            playerToken = -1
        return playerToken
    
    def checkVictory(self, playerNumber, previousMove):
        playerToken = self.getToken(playerNumber)
        x = previousMove[0]
        y = previousMove[1]
        if self.checkMatch(x, y, playerToken, 0):
            self.gameOver = True
        else:
            self.gameOver = False
        
        

def main():
    ConnectFour(3,7)

if __name__ == "__main__":
    main()