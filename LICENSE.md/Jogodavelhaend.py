# Jogo da Velha

import random

def DesTabela(tabela):
    
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
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('Voce quer ser X ou O?')
        letra = input().upper()
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def QuemComeca():
    if random.randint(0, 1) == 0:
        return 'computador'
    else:
        return 'jogador'

def ContinuarJogando():
    print('Quer continuar jogando? (sim ou nao)')
    return input().lower().startswith('s')

def Mover(tabela, letra, numero):
     tabela[numero] = letra

def Ganhador(tabela, letra):
    return ((tabela[7] == letra and tabela[8] == letra and tabela[9] == letra) or 
    (tabela[4] == letra and tabela[5] == letra and tabela[6] == letra) or 
    (tabela[1] == letra and tabela[2] == letra and tabela[3] == letra) or 
    (tabela[7] == letra and tabela[4] == letra and tabela[1] == letra) or 
    (tabela[8] == letra and tabela[5] == letra and tabela[2] == letra) or 
    (tabela[9] == letra and tabela[6] == letra and tabela[3] == letra) or 
    (tabela[7] == letra and tabela[5] == letra and tabela[3] == letra) or 
    (tabela[9] == letra and tabela[5] == letra and tabela[1] == letra)) 

def CopiarTabela(tabela):
    # Make a duplicate of the board list and return it the duplicate.
    dupeTabela = []
    for i in tabela:
        dupeTabela.append(i)
    return dupeTabela

def VerificarJogada(tabela, numero):
    #Verifica se o espaco esta ocupado
    return tabela[numero] == ' '

def MovimentodoJogador(tabela):
    numero = ' '
    while numero not in '1 2 3 4 5 6 7 8 9'.split() or not VerificarJogada(tabela, int(numero)):
        print('Qual o seu movimento? (1-9)')
        numero = input()
    return int(numero)

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
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # IA do computador segue prioridades:
    # 1-Verifica se o computador pode ganhar em um movimento
    for i in range(1, 10):
        copy = CopiarTabela(tabela)
        if VerificarJogada(copy, i):
            Mover(copy, computerLetter, i)
            if Ganhador(copy, computerLetter):
                return i

    #2-Tenta Impedir o Jogador de Ganhar
    for i in range(1, 10):
        copy = CopiarTabela(tabela)
        if VerificarJogada(copy, i):
            Mover(copy, playerLetter, i)
            if Ganhador(copy, playerLetter):
                return i

    #3-Tenta Pegar algum canto se possivel
    numero = JogadasPossiveisComputador(tabela, [1, 3, 7, 9])
    if numero != None:
        return numero

    #4-Tenta Pegar o Centro se Possivel
    if VerificarJogada(tabela, 5):
        return 5

    #5-Move em algum dos lados
    return JogadasPossiveisComputador(tabela, [2, 4, 6, 8])

def TabelaCheia(tabela):
    for i in range(1, 10):
        if VerificarJogada(tabela, i):
            return False
    return True


print('Jogo da Velha')

while True:
    # Reseta a tabela
    ATabela = [' '] * 10
    playerLetter, computerLetter = JogadorLetra()
    turn = QuemComeca()
    print('O ' + turn + ' comeca')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'jogador':
            DesTabela(ATabela)
            numero = MovimentodoJogador(ATabela)
            Mover(ATabela, playerLetter, numero)

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
            numero = MovimentoComputador(ATabela, computerLetter)
            Mover(ATabela, computerLetter, numero)

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
