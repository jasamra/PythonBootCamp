
def display_board(board):
	print(board[1]+'|'+board[2]+'|'+board[3])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[7]+'|'+board[8]+'|'+board[9])


def player_input():
	choice = ''
	while choice != 'X' or choice != 'O':
		try:
			choice = input("player 1:Please pick a marker 'X' or 'O' ").upper()
			if choice == 'X':
				return ('X','O')
			else:
				return ('O','X')
		except:
			print('invalid option')
def space_check(board, position):
	return board[position] == ' '

def place_marker(board, marker, position):

	try:

		board[position] = marker
	except:
		print('error')


def win_check(board, mark):
	#horizontal
	if board[1] == board[2] == board[3] == mark:
		return True
	elif board[4] == board[5] == board[6] == mark:
		return True
	elif board[7] == board[8] == board[9] == mark:
		return True
	#diagonal
	elif board[1] == board[5] == board[9] == mark:
		return True
	elif board[3] == board[5] == board[7] == mark:
		return True
	#vertical
	elif board[1] == board[4] == board[7] == mark:
		return True
	elif board[2] == board[5] == board[8] == mark:
		return True
	elif board[3] == board[6] == board[9] == mark:
		return True
	else:
		return False

import random

def choose_first():
	if random.randint(0, 1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'


def full_board_check(board):
	for i in range(1, 10):
		if board[i] not in ['X','O']:
			return False
	return True

#asks for a player's next position (as a number 1-9)
#uses the function from step 6 to check if it's a free position.
# If it is, then return the position for later use.
def player_choice(board):
	position = 0
	while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
		try:
			position = int(input('Choose your next position: (1-9) '))

		except:
			print('non digit')

	return position

#asks the player if they want to play again and returns a boolean
def replay():
	ask = ''
	while ask not in ['yes', 'no']:
		ask = (input("Play again? ('yes' or 'no')  "))
		if ask == 'yes' or ask == "Yes":
			return True
		elif ask == 'no' or ask == 'No':
			return False
		else:
			pass

def reset_board():
	global test_board,game
	test_board =[' '] * 10
	game = True

#runs game together
print('Welcome to Tic Tac Toe!')
game = True
test_board =[' '] * 10
player1_marker, player2_marker = player_input()
turn = choose_first()
print(turn + ' will go first.')
while game:
	if turn == 'Player 1':
		display_board(test_board)
		position = player_choice(test_board)
		place_marker(test_board, player1_marker, position)
		if full_board_check(test_board):
			display_board(test_board)
			print('The game is a draw!')
			if replay() == False:
				game = False
			else:
				reset_board()


		if win_check(test_board,player1_marker):
			display_board(test_board)
			print('Player 1 is the winner!')
			if replay() == False:
				game = False
			else:
				reset_board()
		else:
			turn = 'Player 2'
	if turn == 'Player 2':
		display_board(test_board)
		position = player_choice(test_board)
		place_marker(test_board, player2_marker, position)
		if full_board_check(test_board):
			display_board(test_board)
			print('The game is a draw!')
			if replay() == False:
				game = False
			else:
				reset_board()

		if win_check(test_board,player2_marker):
			display_board(test_board)
			print('Player 2 is the winner!')
			if replay() == False:
				game = False
			else:
				reset_board()
		else:
			turn = 'Player 1'



