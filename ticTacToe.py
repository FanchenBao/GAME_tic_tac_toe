theBoard = {
			'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
			'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
			'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' ',
			}

def print_board(board):
	''' print the tic-tac-toe board'''
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def check_winner(board):
	''' determine winning situations'''
	if board['top-L'] == board['top-M'] and board['top-L'] == board['top-R']:
		return board['top-L']
	if board['mid-L'] == board['mid-M'] and board['mid-L'] == board['mid-R']:
		return board['mid-L']
	if board['low-L'] == board['low-M'] and board['low-L'] == board['low-R']:
		return board['low-L']
	if board['top-L'] == board['mid-L'] and board['top-L'] == board['low-L']:
		return board['top-L']
	if board['top-M'] == board['mid-M'] and board['top-M'] == board['low-M']:
		return board['top-M']
	if board['top-R'] == board['mid-R'] and board['top-R'] == board['low-R']:
		return board['top-R']
	if board['top-L'] == board['mid-M'] and board['top-L'] == board['low-R']:
		return board['top-L']
	if board['top-R'] == board['mid-M'] and board['top-R'] == board['low-L']:
		return board['top-R']
	return None

def main(board, turn):
	''' main game'''
	i = 1
	for step in range(9):
		print(' ')
		print('The move for ' + turn[i])
		move = input()
		print(' ')
		# check whether input is valid
		if move not in board.keys():
			print('Please input the correct instruction')
			continue
		# check whether move is a duplicate
		if board[move] == ' ':
			board[move] = turn[i]
		else:
			print('That move has already been taken. choose a different move.')
			continue
		print_board(board)
		if step > 3:
			winner = check_winner(board)
			# check whether a three-way match is present
			# check whether the match is real
			if winner and winner != ' ':
				print("winner is " + winner)
				return
		# switch to next turn
		i *= -1

	print('You have tied.')
	return


print("\nLet's play the tic-tac-toe game! Input your move by typing one of the following instructions:")
for k in theBoard.keys():
	print(k, end = ' ')
print(' ')
print_board(theBoard)
turn = {1 : 'O', -1 : 'X'}

main(theBoard, turn)


