player = ""
numberofplay = 0


def MakeBoard():
    return range(9)
    numberofplay = 0


def ShowBoard():
    print board[0], "|", board[1], "|", board[2], "\n", board[3], "|", board[4], "|", board[5], "\n", board[6], "|", \
    board[7], "|", board[8]


def ClearBoard():
    global board
    position = 0
    while position < len(board):
        board[position] = ""
        position += 1


def InGame():
    global board
    status = True
    board = MakeBoard()
    while status:
        print "Choose a position"
        position = CheckInput()
        if CheckPosition(position):
            player = ChangePlayer()
            print "Player", player, "was move, now is time to next"
            board[position] = player
            ShowBoard()
            if CheckWon() is True:
                break
            if numberofplay == 9:
                CheckTie()
                break


def ChangePlayer():
    player1 = "X"
    player2 = "O"
    global player
    global numberofplay
    ingame = True
    while ingame:
        numberofplay += 1
        if player == "":
            player = player1
            return player
        elif player == player1:
            player = player2
            return player
        else:
            player = player1
            return player


def CheckWon():
    if board[0] == board[1] == board[2]:
        print "Player", player, "Win"
        return True
    elif board[3] == board[4] == board[5]:
        print "Player", player, "Win"
        return True
    elif board[6] == board[7] == board[8]:
        print "Player", player, "Win"
        return True
    elif board[0] == board[4] == board[8]:
        print "Player", player, "Win"
        return True
    elif board[2] == board[4] == board[6]:
        print "Player", player, "Win"
        return True
    elif board[0] == board[3] == board[6]:
        print "Player", player, "Win"
        return True
    elif board[1] == board[4] == board[7]:
        print "Player", player, "Win"
        return True
    elif board[2] == board[5] == board[8]:
        print "Player", player, "Win"
        return True
    else:
        return False


def CheckTie():
    print "Nobody win"
    print "Want play again y/n"
    playagain = raw_input()
    if playagain == "y":
        MakeBoard()
        InGame()
    else:
        print "Ok, bye!"


def CheckPosition(position):
    if board[position] == ("O") or board[position] == ("X"):
        print "position occupy, try another"
        return False
    else:
        return True


def CheckInput():
    while True:
        try:
            position = int(raw_input())
        except:
            print "Not a correct value"
            continue
        else:
            return position
            break


InGame()
