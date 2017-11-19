# Tic Tac Toe

import random

def DesTabela(tabela):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + tabela[1] + ' | ' + tabela[2] + ' | ' + tabela[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tabela[4] + ' | ' + tabela[5] + ' | ' + tabela[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tabela[7] + ' | ' + tabela[8] + ' | ' + tabela[9])
    print('   |   |')

def JogadorLetra():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Voce quer ser X ou O?')
        letter = input().upper()
    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def QuemComeca():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'jogador'

def ContinuarJogando():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Quer continuar jogando? (sim ou nao)')
    return input().lower().startswith('s')

def Mover(tabela, letter, move):
     tabela[move] = letter

def Ganhador(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
def CopiarTabela(tabela):
    # Make a duplicate of the board list and return it the duplicate.
    dupeTabela = []
    for i in tabela:
        dupeTabela.append(i)
    return dupeTabela

def VerificarJogada(tabela, move):
    # Return true if the passed move is free on the passed board.
    return tabela[move] == ' '

def MovimentodoJogador(tabela):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not VerificarJogada(tabela, int(move)):
        print('Qual o seu movimento? (1-9)')
        move = input()
    return int(move)

def JogadasPossiveisComputador(tabela, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if VerificarJogada(tabela, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def MovimentoComputador(tabela, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = CopiarTabela(tabela)
        if VerificarJogada(copy, i):
            Mover(copy, computerLetter, i)
            if Ganhador(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = CopiarTabela(tabela)
        if VerificarJogada(copy, i):
            Mover(copy, playerLetter, i)
            if Ganhador(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = JogadasPossiveisComputador(tabela, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if VerificarJogada(board, 5):
        return 5
    # Move on one of the sides.
    return JogadasPossiveisComputador(tabela, [2, 4, 6, 8])

def TabelaCheia(tabela):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if VerificarJogada(tabela, i):
            return False
    return True


print('Jogo da Velha')

while True:
    # Reset the board
    ATabela = [' '] * 10
    playerLetter, computerLetter = JogadorLetra()
    turn = QuemComeca()
    print('O ' + turn + ' comeca')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'jogador':
            # Player’s turn.
            DesTabela(ATabela)
            move = MovimentodoJogador(ATabela)
            Mover(ATabela, playerLetter, move)

            if Ganhador(ATabela, playerLetter):
                DesTabela(ATabela)
                print('Voce ganhou')
                gameIsPlaying = False
            else:
                if TabelaCheia(ATabela):
                    DesTabela(ATabela)
                    print('Deu Velha')
                    break
                else:
                    turn = 'computador'
        else:
            # Computer’s turn.
            move = MovimentoComputador(ATabela, computerLetter)
            Mover(ATabela, computerLetter, move)

            if Ganhador(ATabela, computerLetter):
                DesTabela(ATabela)
                print('Computador Ganhou')
                gameIsPlaying = False
            else:
                if TabelaCheia(ATabela):
                    drawBoard(ATabela)
                    print('Deu Velha')
                    break
                else:
                    turn = 'jogador'
    if not ContinuarJogando():
        break
