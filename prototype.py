import random # random module for random selection


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
	"""
	Args :
		hand -> list object 
	return : None
	"""
	
	pass

def IsBlackJack(hand):
	"""
	Args :
		hand -> list object 
	
	return : Boolean
	

	""" 
	pass

def YesOrNo(message = ""):
	"""
	Args :
		message -> string object 

	return : Boolean
	""" 
	# ask for a Yes or No response

	pass 

def DealHand(hand):
	"""
	Args :
		hand- list object 
	return None
	""" 
	# add a random card to the hand


	pass 



def PlayGame():
	"""
	return : None"""
	# main function to pay the game
	# contains loops and logical statements to simulate a blackjack game
	pass 


if __name__ == '__main__':
	PlayGame()
