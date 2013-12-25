  
#!/bin/python

### This is the test script for the Database Application 
### By Gary Cheung
### 
from SoloBlackjack import *
import unittest

            
    

## CREATE A TEST FILE 
class testCardsGame(unittest.TestCase):

    bj = blackjack()
    
    def checkCards(self):
        card1 = Card("10", "H")
        self.assertEqual("10", card1.get_rank() )
        self.assertEqual("H", card1.get_suit() )

    def testCheckDeck(self):
        cardDeckTest = Deck()
        
        #Test Return Deck
        cardsListTest=  cardDeckTest.get_deck()
        self.assertEqual(48, len(cardsListTest))
        
        
        #Test Shuffle
        self.assertEqual("A,H", str(cardsListTest[0]))

        cardDeckTest.shuffle()
        self.assertNotEqual("A,H", str(cardsListTest[0]))
        
        # Test Deal

    def testCreateBoard(self):
        self.assertEqual(dict, type(blackjack().createBoard()))
        self.assertEqual(4, len(blackjack().createBoard()))


#ChecList
#Check Boat
#Check Location

    def testAddToBoard(self):
        testBoard = blackjack().createBoard()
        blackjack().addToBoard(testBoard,1,1,"test")
        self.assertEqual("test" , testBoard[1][1])

    def testCheckBoard(self):
        testBoard = blackjack().createBoard()
        blackjack().addToBoard(testBoard,1,1,"test")
        
        self.assertEqual(False , blackjack().checkBoard(testBoard,"test"))
        self.assertEqual(True , blackjack().checkBoard(testBoard,""))
        
        
    
    def testCheckLocation(self):
        """ Testing to see if this fucntion correctly checks to see that 
        Also: Since last and firstPosition in Row 4 and Row 3 are unaccesible
        on the game board, it checks to make sure those positions are not entered"""
        self.locationTracker = [[1,2],[2,3],[2,2]]

        self.assertEqual(False , blackjack().checkLocation(self.locationTracker,1,2))
        self.assertEqual(False , blackjack().checkLocation(self.locationTracker,2,3))
        self.assertEqual(False , blackjack().checkLocation(self.locationTracker,2,3))
        
        self.assertEqual(True , blackjack().checkLocation(self.locationTracker,10000,100000))
        self.assertEqual(True , blackjack().checkLocation(self.locationTracker,-10000,-100000))
        
        self.assertEqual(False , blackjack().checkLocation(self.locationTracker,4,1))
        self.assertEqual(False , blackjack().checkLocation(self.locationTracker,4,5))
        self.assertEqual(False , blackjack().checkLocation(self.locationTracker,3,1))
        self.assertEqual(False , blackjack().checkLocation(self.locationTracker,3,5))
     
    def testWrongSize(self):
        """ Check to see if the input is larger than the board, if yes, then return True. 
        If it is not return false"""
        self.board = blackjack().createBoard()
        self.assertNotEqual(True , blackjack().wrongSize(1,1,self.board)) 
        self.assertEqual(True , blackjack().wrongSize(1000000,1000000,self.board)) 
        self.assertEqual(True , blackjack().wrongSize(-1000000,-1000000,self.board)) 
          
    def testNotInt(self):
        """ Test that it is not an interger, returns true if not int"""
        self.assertEqual(True , blackjack().notInteger("row","column")) 
        self.assertEqual(False, blackjack().notInteger("100000","100000"))       
        self.assertEqual(False , blackjack().notInteger("10","15"))          
     
    def testDiscard(self):
        """ Test to see if the Discard WOrks Properly"""
        self.testBoard = blackjack().createBoard()
        self.discard = [1,2,3,4]
        self.currentCard = ["1,S"]
        
        self.assertEqual([["1,S"],2,3,4] , blackjack().discardCard(self.testBoard,self.discard,self.currentCard) )
        
        self.currentCard = ["TESTCARD"]   
        self.assertEqual([["1,S"],["TESTCARD"],3,4] , blackjack().discardCard(self.testBoard,self.discard,self.currentCard) )            
        
            
    def testSumRows(self):
        """ Tests a Normal Board, and Board with Extreme Value to see if Sum Row returns correct value.
        Note if the Sum Wihout Ace is greater than 21, retruns that value imediately (since further computation is
        not nessecary)
        """
        self.board = {1:[ Card("A","S"), Card(1,"A") , Card("A","A") , Card(4,"S")  ,Card("Q","S")],
                 2:[ Card("A","S"), Card(10,"A") , Card("A","A") , Card(4,"S")  ,Card("Q","S")],
                 3:[ Card(5,"S"), Card(1,"A") , Card("A","A") , Card(4,"S")  ,Card("Q","S")],
                 4:[ Card(1,"S"), Card(1,"A") , Card("A","A") , Card("Q","S")  ,Card("Q","S")]}
        self.assertEqual([17,24,21,22] , blackjack().sumRows(self.board) )
        
        self.board = {1:[ Card("A","S"), Card("A","A") , Card("A","A") , Card("A","S")  ,Card("A","S")],
                 2:[ Card("A","S"), Card(10,"A") , Card("A","A") , Card(2,"S")  ,Card("Q","S")],
                 3:[ Card(5,"S"), Card(1,"A") , Card("A","A") , Card(4,"S")  ,Card("Q","S")],
                 4:[ Card(1,"S"), Card(1,"A") , Card("A","A") , Card(100,"S")  ,Card(100,"S")]}
        self.assertEqual([15,22,21,202] , blackjack().sumRows(self.board) )
    #sef testSumColums(self):        
    
    def testSumColumns(self):
        """ Tests a Normal Board, and Board with Extreme Value to see if Sum Columns returns correct value.
        Note if the Sum Wihout Ace is greater than 21, retruns that value imediately (since further computation is
        not nessecary)
        """
        self.board = {1:[ Card("A","S"), Card(1,"A") , Card(9,"A") , Card(4,"S")  ,Card(5,"S")],
                     2:[ Card("A","S"), Card(1,"A") , Card(1,"A") , Card(4,"S")  ,Card(1,"S")],
                     3:[ "X",          Card(1,"A") , Card("A","A") , Card(4,"S")  ,"X"],
                     4:[ "X",          Card(1,"A") , Card(10,"A") , Card("A","S")  ,"X"]}
        self.assertEqual([12,4,21,13,6] , blackjack().sumColumns(self.board) )
        
        self.board = {1:[ Card("A","S"), Card("A","A") , Card("A","A") , Card(4,"S")  ,Card(10,"S")],
                     2:[ Card("A","S"), Card("A","A") , Card(100,"A") , Card("A","S")  ,Card(10,"S")],
                     3:[ "X",          Card("A","A") , Card("A","A") , Card(4,"S")  ,"X"],
                     4:[ "X",          Card("A","A") , Card(100,"A") , Card("A","S")  ,"X"]}
        self.assertEqual([12,14,200,20,20] , blackjack().sumColumns(self.board) )
            
    def testScoreHand(self):
        """Using the Sum of the Rows and Columns,
        It returns a score for each Row and Column based on the scoring rubric
        """
        self.board = {1:[ Card("A","S"), Card(1,"A") , Card(9,"A") , Card(4,"S")  ,Card(5,"S")],
                     2:[ Card("A","S"), Card(1,"A") , Card(1,"A") , Card(4,"S")  ,Card(1,"S")],
                     3:[ "X",          Card(1,"A") , Card("A","A") , Card(4,"S")  ,"X"],
                     4:[ "X",          Card(1,"A") , Card(10,"A") , Card("A","S")  ,"X"]}
                     #12+4+21+6
                     #20+17+16+21
                     #2+7+1 = 10  5+2+1+7=15
                     
        self.assertEqual( 21 , blackjack().scoreHand(self.board) )
    
        self.board2 = {1:[ Card("A","S"), Card("A","A") , Card(1,"A") , Card(4,"S")  ,Card(4,"S")],
                     2:[ Card("A","S"), Card("A","A") , Card(1,"A") , Card(4,"S")  ,Card(1,"S")],
                     3:[ "X",          Card("A","A") , Card(1,"A") , Card(4,"S")  ,"X"],
                     4:[ "X",          Card("A","A") , Card(1,"A") , Card("A","S")  ,"X"]}

        
        self.assertEqual( 17 , blackjack().scoreHand(self.board2) )             
                         
            
if __name__ == '__main__':
    unittest.main()
    

    