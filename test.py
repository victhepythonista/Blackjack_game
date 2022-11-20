# run this script to perform tests on the BlACKJACK GAME 


from game import *


 

def test_IsBlackJack():
	# test if the IsBlackjack function can identify if  a 
	# hand is blackjack... 
	hand = [10,11] # this hand is  blackjack 
	false_hand = [7,6] # this hand is not  blackjack
	print("function_test :   IsBlackJack   - ", end= "") 

	if IsBlackJack(hand) and not IsBlackJack(false_hand):
		print("  ok -")
	else:
		print("  FAIL ")


def test_AdjustAceValue():
	# test if AdjustAce value function changes the value of an ace 
	# if the total sum of the hand is more than 21 
	print("function_test :   AdjustAceValue   - ", end= "") 

	test_hand = [11,6,9]
	test_hand = AdjustAceValue(test_hand)

	target_total = 16  # this is the new sum of the hand if the ace in the deck is changed to a value of 1
	if sum(test_hand) == target_total:
		print("  OK -")
	else:
		print("  FAIL -")





def test_DealHand():
	# test the DealHand function 
	# if ok it should add a new random card ti the hand
	hand   = []
	DealHand(hand)
	print("function_test :   DealHand- ", end= "") 
	if len(hand) == 2 :
		print("OK ")
	else:
		print("FAIL")

def RunAllTests():
	test_DealHand()
	test_IsBlackJack()
	test_AdjustAceValue()

 
if __name__ == '__main__':
	RunAllTests()