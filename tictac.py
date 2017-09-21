board = range(9)

def ShowBoard():
	print board[0],"|", board[1], "|", board[2] , "\n" , board[3], "|" ,board[4], "|", board[5], "\n",  board[6], "|", board[7], "|", board[8] 

def ClearBoard():
	global board
	position = 0  
	while position < len(board):
		board[position] = ""
		position +=1
	
def InGame():
	global board
	player1 = "X"
	player2 = "O"
	status = False
	while status is False: 
		print "Choose a position"
		position = int(raw_input())
		board[position] = player1 
		#status = False
		ShowBoard()
		if CheckWon() is True:
			break

def CheckWon():
	if board[0] == board[1] == board[2]:
		print "End Game Someone Win"
		return True
	elif board[3] == board[4] == board[5]:
		print "End Game someone win"
		return True
	elif board[6] == board[7] == board[8]:
		print "End Game someone win"
		return True
	else: 
		return False

ShowBoard()
InGame()
CheckWon()
ClearBoard()
ShowBoard()
