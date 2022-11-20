# run this script to perform tests on the BlACKJACK GAME 

import unittest


from game import *



class BlackjackGameTest(unittest.TestCase):



	def test_DealHand(self):
		# test the DealHand function 
		# if ok it should add a new random card ti the hand
		hand   = []
		DealHand(hand)
		self.assertIsInstance( hand , list )



	def test_IsBlackJack(self):
		# test if the IsBlackjack function can identify if  a 
		# hand is blackjack... 
		hand = [10,11] # this hand is  blackjack 
		false_hand = [7,6] # this hand is not  blackjack
		self.assertTrue(IsBlackJack(hand))
		self.assertFalse(IsBlackJack(false_hand))

	def test_AdjustAceValue(self):
		# test if AdjustAce value function changes the value of an ace 
		# if the total sum of the hand is more than 21 
		test_hand = [11,6,9]
		test_hand = AdjustAceValue(test_hand)

		target_total = 16  # this is the new sum of the hand if the ace in the deck is changed to a value of 1

		self.assertEqual(sum(test_hand), target_total)





if __name__ == '__main__':
	unittest.main()