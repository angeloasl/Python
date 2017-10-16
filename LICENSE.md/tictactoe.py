def makeBoard() :
    theBoard = {};
    rows = ['1','2','3']
    cols = ['1','2','3']
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            theBoard.setdefault(key,False)
    print('DEBUG: '+str(theBoard))
    return theBoard

def printCell(cell) :
    if cell : 
        return ' '+str(cell)+' '
    else :
        return '   '

def showBoard(board) : 
    print(printCell(board['1-1'])+'|'+printCell(board['1-2'])+'|'+printCell(board['1-3']))
    print('-----------')
    print(printCell(board['2-1'])+'|'+printCell(board['2-2'])+'|'+printCell(board['2-3']))
    print('-----------')
    print(printCell(board['3-1'])+'|'+printCell(board['3-2'])+'|'+printCell(board['3-3']))

def determineVictory(board):
    rows = ['1','2','3']
    cols = ['1','2','3']
    # se uma linha tiver todas as colunas iguais é vitoria
    for r in rows :
        col1 = str(r)+'-1'
        col2 = str(r)+'-2'
        col3 = str(r)+'-3'
        if board[col1] == board[col2] == board[col3] and bool(board[col1]) :
            return board[col3]
    # se uma coluna tiver todas as linhas iguais é vitoria
    for c in cols :
        row1 = '1-'+str(c)
        row2 = '2-'+str(c)
        row3 = '3-'+str(c)
        if board[row1] == board[row2] == board[row3] and bool(board[row1]) :
            return board[row3]
    # se houver uma diagonal com todas iguais então é vitoria
    middle = '2-2';
    sel1, sel2 = str(rows[0]+'-'+cols[2]), str(rows[2]+'-'+cols[0])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    sel1, sel2 = str(rows[0]+'-'+cols[0]), str(rows[2]+'-'+cols[2])
    if board[middle] == board[sel1] == board[sel2] :
       return board[middle]
    return False

def determineAvailableMoves(board) :
    rows = ['1','2','3']
    cols = ['1','2','3']
    hasMoves = False
    # verifica se posicão escolhida é válida
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            if not bool(board[key]) :
                return True
    return hasMoves

def readInputAndTryToPutOnBoard(board, player) :
    rows = ['1','2','3']
    cols = ['1','2','3']
    print('To make a move type an row (1, 2, 3), followed by a dash (-), and an column (1, 2, 3), like 1-2')
    move = input()
    valida = False
    # verifica se posicão escolhida é válida
    for r in rows :
        for c in cols :
            key = str(r) + '-' + str(c)
            if key == move :
                valida = True

    if valida & bool(board[move]):
        print('Position already taken!');
        return False
    elif valida : 
        board[move] = player
        return True
    else : 
        print('Invalid position!');
        return False

def changePlayer(player) :
    if player == 'X':
        print('Player O turn!')
        return 'O'
    else :
        print('Player X turn!')
        return 'X'
    
def game():
    print('Lets play a game, X goes first, O goes after!')
    player = 'X'
    board = makeBoard();
    while True :
        showBoard(board);
        # Obtem movimento
        while True : 
            move = readInputAndTryToPutOnBoard(board, player)
            if move :
                break
        # Verifica se movimento concedeu vitoria
        if determineVictory(board) :
            showBoard(board);
            print('Player '+player+' wins!!!')
            return True
        # verifica se ainda há movimentos possíveis
        if not determineAvailableMoves(board) :
            print('Draw, or like we say in Brazil, deu velha...')
            return True
        # caso não tenha vencido então muda jogador e tenta denovo
        player = changePlayer(player)
        
game();
