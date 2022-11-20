import random


INTRO = """
__________________________________________________

		 BLACKJACK GAME 
_________________________________________________
		"""
RESULT_INFO = f"""

   {'*-'*15}

	FINAL RESULT 	: 	%s 

	PLAYER CARDS	: 	%s 	 TOTAL = %s

	DEALER CARDS 	: 	%s   TOTAL = %s

   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   _______________________________"""

ROUND_INFO = """

	 ***************************************
	 -------- ROUND RESULT--------------

		PLAYER CARDS	: 	%s 	TOTAL = %s

		DEALER CARDS	: 	%s   
	-----------------------------------------
	*****************************************"""
PROGRAM_RUNNNING = True 
ROUND_RUNNING = True
RESULT = ""

DECK = [11, 2,3,4,5,6,7,8,9,10,10,10,10]

def AdjustAceValue(hand):
	'''
	args : hand -> list 

	return : list
	'''
	
	# if an ace(11) in the deck and the value is over 21
	# the ace is set to a value of 1 
	if not sum(hand) > 21:
		return hand

	if 11 in hand:
		hand[hand.index(11)] = 1 
		return hand 


def IsBlackJack(hand):
	'''
	args 		: hand -> list 

	return 	: Bool'''
	# hand is a ist of cards of a user
	# True if blackjack else False 

	if sum(hand) == 21:
		return True 
	return False 


def YesOrNo(message = ""):
	# displays the [message] parameter and
	# asks a user for a yes or no choice
	while True:
		choice = input(message + " \n  [y] for yes |  [N] for no \n")
		c = choice.lower()
		if c == "y":
			return True 
		elif c == "n":
			return False


def DealHand(hand):
	'''
	args 		: hand -> list 

	return 	: None'''
	# add a random card to the hand

	if hand == []:

		for i in range(2):
			hand.append(random.choice(DECK))
	else:
		hand.append(random.choice(DECK))




def PlayGame():

	# main game function
	print(INTRO) # print out the introduction 
	DEAL_PLAYER = True

	while PROGRAM_RUNNNING:
		# main loop 
		print("  -- STARTING NEW GAME --" )	
		input("     |   click ENTER  to start  |  ")
		player_hand = []
		dealer_hand = [] 
		ROUND_COUNT = 0
		while ROUND_RUNNING:
			# round loop

			if DEAL_PLAYER:
				DealHand(player_hand)
			DealHand(dealer_hand)

			AdjustAceValue(player_hand)
			player_total = sum(player_hand)
			dealer_total = sum(dealer_hand)
			print(ROUND_INFO % (player_hand,player_total, dealer_hand[0:-1]))
			if sum(player_hand) > 21:
				RESULT = "LOST"
				break

			if IsBlackJack(player_hand):
				if IsBlackJack(dealer_hand):
					RESULT = "DRAW"
					break 
				else:
					RESULT = 'WIN'
					break
			else:
				if sum(dealer_hand) > 16:
					if player_total == dealer_total:
						RESULT = 'DRAW'
						break
					if IsBlackJack(player_hand) and IsBlackJack(dealer_hand):
						RESULT = "DRAW"
						break
					if dealer_total > player_total:
						RESULT  = "LOST"
						break
					
					else:
						RESULT = "WIN"
						break
				else:

					choice = YesOrNo("Pick Another card ?")
					if choice:
						DEAL_PLAYER = True 
						continue 
					else:
						DEAL_PLAYER = False
						continue


	 

	 

		print(RESULT_INFO % (RESULT,player_hand, player_total , dealer_hand, dealer_total))
		DEAL_PLAYER = True
		if YesOrNo("Start new game ?"):
			continue
		else:
			print("ENDING GAME --")
			break

if __name__ == '__main__':
	PlayGame()
