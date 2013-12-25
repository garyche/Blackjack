#!/bin/python
from cards import *

## By : Gary Cheung

class blackjack(object):
 
    def __init__(self):

        self.cardDeck = Deck()
        self.cardsList=  self.cardDeck.get_deck()
        
        self.board = self.createBoard()


    def createBoard(self):
        """ Creates a board when called, returns a board as a dictionary of lists"""
        self.board = {}
    
        self.row1 = [1,2,3,4,5]
        self.board[1] = self.row1
    
        self.row2 = [6,7,8,9,10]
        self.board[2] = self.row2
    
        self.row3 = ["X",11,12,13,"X"]
        self.board[3] = self.row3
    
        self.row4 = ["X",14,15,16,"X"]
        self.board[4]  = self.row4
    
        return self.board
    

    

        
    def displayBoard(self,board):
        
        self.board = board
        """ Displays the contents of a board in a formatted form when called. """
    
    #    self.row1 = next(board.itervalues())
        print "       1 |  2  |  3  |  4  |  5  |"

    
        for rows in self.board:
        
            self.output = str(rows) + " : " + "| "
        
            for item in self.board[rows]:
                self.output = self.output + "(" + str(item) + ")" + (" | ")
            
            #output = output + " ]"    
            print self.output


    def checkBoard(self,board,value):
        """ Functions Checks the Board and if the value is currently in the board, it returns False"""
        self.value = value
        self.board = board
        
        for row in self.board:
            row = self.board[row]
            for column in row:
                if self.value == column:
                    return False
        return True

    def checkLocation(self,locationTracker,row,column):
        """ This Function Checks the Locaiton Array to see if the row or column is already exsistant. It returns 0 
        if it is in the locationTracker list, and return 1 otherwise"""
        self.row = row
        self.column = column
        self.locationTracker = locationTracker
        
        if (self.row == 3 and (self.column == 1 or self.column == 5)) or ( self.row == 4 and  (self.column == 1 or self.column == 5)) :
            return False
            
            
        for location in self.locationTracker:
            #location.split(",")
            self.locationRow = location[0]
            self.locationColumn = location[1]
        
            if self.row == int(self.locationRow) and self.column == int(self.locationColumn):
                return False
        return True


    def wrongSize(self,row,column,board):
        """ Check to see if the user input size of Row and Column is larger than the board, if yes, returns True"""
        self.row = row
        self.column = column
        self.board = board
        
        
        if self.row < 1 or self.column < 1:
            return True
        
        elif len(self.board) < self.row :
            return True
    
        if self.column > len(self.board[self.row]):
            return True
    
        return False

    


    def notInteger(self,row,column):
        self.row = row
        self.column = column
 
        """ Check If User Input is a Integer"""
        if str(self.column).isdigit() and str(self.row).isdigit():     
            return False
        else:
            return True  
    
   

    def checkError(self,board,row,column,locationTracker,currentCard):
        """ This funciton check for user input error, and will reprompt user if there is an error."""
        
        self.row = row
        self.column = column
        self.board = board
        self.locationTracker = locationTracker
        self.currentCard = currentCard
        
        self.error = True 
    
        while (self.error):
        
            if  self.row == "" or self.column == "":
            
                print "Error: Wrong Input Type"  
                self.row = raw_input("What Row Do You Want To Place The Card, (D for Discard)")
                self.column = raw_input("What Column Should We Place The Card")
                self.error = True 
                continue 
    
            if self.notInteger(self.row,self.column):
                print "Error: Please Input A Number" 
                self.row = raw_input("What Row Do You Want To Place The Card, (D for Discard)")
                self.column = raw_input("What Column Should We Place The Card")
                self.error = True 
                continue

            if self.checkLocation(self.locationTracker,int(self.row),int(self.column))==False or self.checkBoard(self.board, self.currentCard)==False:

                print "Error: This location has alread been chosen" 
                self.row = raw_input("What Row Do You Want To Place The Card, (D for Discard)")
                self.column = raw_input("What Column Should We Place The Card") 
                self.error = True 
                continue
        
            if self.wrongSize(int(self.row),int(self.column),self.board):
                print "Error: The input size is wrong" 
                self.row = raw_input("What Row Do You Want To Place The Card, (D for Discard)")
                self.column = raw_input("What Column Should We Place The Card")
                self.error = True 
                continue
            self.error = False 
            return(self.board,self.row,self.column) 

    


    def addToBoard(self,board,row,column,value):
        self.row = row
        self.column = column
        self.board = board
        self.value = value

        
        self.boardRow = self.board[self.row]
        if self.boardRow[self.column] == self.value:
            return 0
        else:
            self.boardRow[self.column] = self.value
    
    
    
    def discardCard(self,board,discard,currentCard):
        
        self.discard = discard
        self.board = board
        self.currentCard = currentCard
        
        """ This function will place the current card object in the discard list, will print the discard object and returns null """
        for i in range(len(self.discard)):
            if type(self.discard[i]) == int:
                self.discard[i] = self.currentCard
                break
        return self.discard
    
    def welcome(self):
        """ Displays The Welcome Message, returns null"""
    
        print "Welcome To The Poker Solitare Game"
        print "Here are the instructions:"
        print "Please Select a Location, Row and Column, on the Board to place your card"
        print "If you want to discard your card please select: D"
    
    #########
    ###
    ####
    def rankConvert(self,rank):
        """ Converts the J Q K to 10's"""
        self.rank = rank
        self.out = rank
        if self.rank == "J":
            self.out = 10
        elif self.rank == "Q":
            self.out = 10
        elif self.rank == "K":
            self.out = 10
        return self.out 


    def sumRows(self,board):
        """ Returns The sum of each row, If the sum (without ace is greater than 21), immediately appends this value to the list
        if the sum has aces and before ace, is less than 21, will evaluate whether the ace should be 11 or 1, and return appen better
        value to the list, will return a list of value for each row"""
        self.rowList = []
    
        for rows in board:
        
            self.countA = 0
            self.sumRow = 0
            for card in board[rows]:
                
                if card == "X":
                    continue 
                    
                self.rank = card.get_rank()

                self.rank = self.rankConvert(self.rank)
              #  print self.rank
            
                if self.rank == "A":
                    self.countA = self.countA + 1    
                    continue
            
                self.sumRow = self.sumRow + self.rank 
            
            if self.sumRow > 21:
                self.rowList.append( self.sumRow)
                continue
            
           # print str(rows) + " "+str(self.countA)
        
            if self.countA > 0:
                self.testScore = self.sumRow
                self.testScore2 = self.sumRow
            
      
                for i in range(self.countA):
           
                    if i == 0:
                        self.testScore = self.testScore + 11
                    else: 
                        self.testScore = self.testScore + 1
 
            
                for i in range(self.countA):
                    self.testScore2 = self.testScore2 + 1

                self.compare1 = 21 - self.testScore 
                self.compare2 = 21 - self.testScore2 
            

                if self.compare1<0: 
                    if self.compare2>=0:
                        self.rowList.append(self.testScore2)
                        continue
                elif self.compare2<0:
                    if self.compare1>=0:
                        self.rowList.append(self.testScore1)
                        continue
                
                if self.compare1 < self.compare2:
                    self.sumRow =  self.testScore
                else:
                    self.sumRow = self.testScore2
                
                self.rowList.append(self.sumRow)
        return self.rowList
    
    def sumColumns(self,board):
        """ Sums the Score, takes it into account Aces are 1 or 11, and Append scores to a list,
        If the score without ace is greater than 21, that is appended to the list,
        if the Score is on the 1st or 5th COLUMN IT WILL ONLY GO DOWN 2 ROWS AS THAT IS the nature of the
        board"""
        self.list = []
        self.countA = 0
        self.board = board

        for i in range(5):

      
            self.sumColumn = 0
            self.countA = 0
        
            for row in board:
         
                if row == 3 or row == 4:
                    if i == 0 or i == 4:
                         continue
            
            
                self.card =board[row][i]
            
                self.rank = self.card.get_rank()
      
                self.rank = self.rankConvert(self.rank)
                #print self.rank
            
                if self.rank == "A":
                    self.countA = self.countA + 1    
                    continue
         
                self.sumColumn = self.sumColumn + self.rank 
            
 

            if self.sumColumn > 21:
                self.list.append(self.sumColumn)

                continue

            if self.countA > 0:
                self.testScore = self.sumColumn
                self.testScore2 = self.sumColumn
            
      
                for i in range(self.countA):
           
                    if i == 0:
                        self.testScore = self.testScore + 11
                    else: 
                        self.testScore = self.testScore + 1
 
            
                for i in range(self.countA):
                    self.testScore2 = self.testScore2 + 1

                self.compare1 = 21 - self.testScore 
                self.compare2 = 21 - self.testScore2 
            

             #   print self.testScore
              #  print self.testScore2
            
                if self.compare1<0: 
                    if self.compare2>=0:
                        self.list.append(self.testScore2)
                        continue
                elif self.compare2<0:
                    if self.compare1>=0:
                        self.list.append(self.testScore1)
                        continue
                
                
                if self.compare1 < self.compare2:
                    self.sumColumn =  self.testScore
                else:
                    self.sumColumn = self.testScore2
            
            self.list.append(self.sumColumn)    
        
        return self.list     
    
    
    def scoreHand(self,board) :
        """ Calculate the score of each hand and returns the score """
        self.board = board

        score = 0
        col = self.sumColumns(board)
        rows = self.sumRows(board)

        
        for colScore in col:
            if colScore == 21 :
                score = score + 7
            elif colScore == 20 :
                score = score + 5
            elif colScore == 19 :
                score = score + 4
            elif colScore == 18 :
                score = score+ 3
            elif colScore == 17 :
                score = score + 2
            elif colScore < 17 :
                score = score + 1
            else :
                score = score + 0
                continue

            
        for rowScore in rows:
            if rowScore == 21 :
                score = score + 7
            elif rowScore == 20 :
                score = score + 5
            elif rowScore == 19 :
                score = score + 4
            elif rowScore == 18 :
                score = score+ 3
            elif rowScore == 17 :
                score = score + 2
            elif rowScore < 17 :
                score = score + 1
            else :
                score = score + 0
        return score
    
                
    def outputDiscard(self,discard):
        """ Return the Discard List in formatted form """
        self.discard = discard
        
        out2 = "Discard: "
        for items in self.discard:
            out2 = out2 + " |" + str(items) + "|"
        return out2
        
    def play(self):
        self.welcome()

        self.discard = [17,18,19,20]
        self.discardCount = 0
        self.locationTracker = []
        
        self.displayBoard(self.board)
        print self.discard
        
        while (len(self.locationTracker)<16):

            self.shuffle = self.cardDeck.shuffle()
            self.currentCard = self.cardDeck.deal()
            
            print "You card is " + str(self.currentCard)
        

            self.row = raw_input("What Row Do You Want To Place The Card, (D for Discard)")
        

            if (self.discardCount >= 4):
                next
            elif self.row == "D":
                self.displayBoard(self.board)
                self.discardCard(self.board,self.discard,self.currentCard)
                
                print self.outputDiscard(self.discard)
                self.discardCount = self.discardCount + 1
                continue
    
            self.column = raw_input("What Column Should We Place The Card")
        
            if (self.discardCount >= 4):
                next
            elif self.column == "D":
                self.discardCard(self.board,self.discard,self.currentCard)
                self.displayBoard(self.board)
                print self.outputDiscard(self.discard)
                self.discardCount = self.discardCount + 1
                continue
            
            
            self.board,self.row,self.column = self.checkError(self.board,self.row,self.column,self.locationTracker,self.currentCard)
         
            if self.row == "D" or self.column =="D":
                if self.discardCount >= 4:
                    self.discardCard(self.board,self.discard,self.currentCard)
                    print self.outputDiscard(self.discard)
                    continue 
      
        
            
            self.column = int(self.column) - 1
        
        
            self.location = [int(self.row),int(self.column) +1 ]
            self.locationTracker.append(self.location)
            self.addToBoard(self.board,int(self.row),int(self.column),self.currentCard)

            self.displayBoard(self.board)
            
            print self.outputDiscard(self.discard)

            
            
        print "Score is:"
        print self.scoreHand(self.board)
        
blackjack().play()
