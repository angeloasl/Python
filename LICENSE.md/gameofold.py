placar1 = [3, 3, 3]
placar2 = [3, 3, 3]
placar3 = [3, 3, 3]


def mirror(placar1, placar2, placar3):
    for k in range(0, 3):
        if (linha1[k] == usuario):
            placar1[k] = 5

        if (linha2[k] == usuario):
            placar2[k] = 5

        if (linha3[k] == usuario):
            placar3[k] = 5

        if (linha1[k] == oponente):
            placar1[k] = 2

        if (linha2[k] == oponente):
            placar2[k] = 2

        if (linha3[k] == oponente):
            placar3[k] = 2
    return

def atualizatela(linha1, linha2, linha3):
    print('''a)  %s  | b)  %s  | c)  %s
------------------------------- ''' % (linha1[0], linha1[1], linha1[2]))
    print('''d)  %s  | e)  %s  | f)  %s
------------------------------- ''' % (linha2[0], linha2[1], linha2[2]))
    print('''g)  %s  | h)  %s  | i)  %s   ''' % (linha3[0], linha3[1], linha3[2]))


    return

def vitoria(placar1, placar2, placar3):
    game = True
    if ((placar1[0] * placar1[1] * placar1[2] == 125) or (placar2[0] * placar2[1] * placar2[2] == 125) or (
                        placar3[0] * placar3[1] * placar3[2] == 125) or (placar1[0] * placar2[0] * placar3[0] == 125) or (
                        placar1[1] * placar2[1] *placar3[1] == 125) or (placar1[2] * placar2[2] * placar3[2] == 125) or (
                        placar1[2] * placar2[1] * placar3[0] == 125) or (placar1[0] *placar2[1] *placar3[2] == 125)):
        print("Usuario venceu!")
        game = False

    if (cont == 9):

        if ((placar1[0] * placar1[1] * placar1[2] != 125) or (placar2[0] * placar2[1] * placar2[2] != 125) or (
                            placar3[0] * placar3[1] * placar3[2] != 125) or (placar1[0] * placar2[0] * placar3[0] != 125) or (
                            placar1[1] * placar2[1] *placar3[1] != 125) or (placar1[2] * placar2[2] * placar3[2] != 125) or (
                            placar1[2] * placar2[1] * placar3[0] != 125) or (placar1[0] *placar2[1] *placar3[2] != 125) or (placar1[0] * placar1[1] * placar1[2] != 8) or (placar2[0] * placar2[1] * placar2[2] != 8) or (
                            placar3[0] * placar3[1] * placar3[2] != 8) or (placar1[0] *placar2[0] * placar3[0] != 8) or (
                            placar1[1] *placar2[1] *placar3[1] != 8) or (placar1[2] * placar2[2] * placar3[2] != 8) or (
                            placar1[2] * placar2[1] * placar3[0] != 8) or (placar1[0] * placar2[1] * placar3[2] != 8)):
            print("Deu velha")

    if ((placar1[0] * placar1[1] * placar1[2] == 8) or (placar2[0] * placar2[1] * placar2[2] == 8) or (
                        placar3[0] * placar3[1] * placar3[2] == 8) or (placar1[0] *placar2[0] * placar3[0] == 8) or (
                        placar1[1] *placar2[1] *placar3[1] == 8) or (placar1[2] * placar2[2] * placar3[2] == 8) or (
                        placar1[2] * placar2[1] * placar3[0] == 8) or (placar1[0] * placar2[1] * placar3[2] == 8)):
        print("Oponente venceu!")
        print("Jogada numero ", cont)
        game = False

    return game

def escreve_usuario(jogada):
    if (jogada == 'a'):
        linha1[0] = usuario
    if (jogada == 'b'):
        linha1[1] = usuario
    if (jogada == 'c'):
        linha1[2] = usuario
    if (jogada == 'd'):
        linha2[0] = usuario
    if (jogada == 'e'):
        linha2[1] = usuario
    if (jogada == 'f'):
        linha2[2] = usuario
    if (jogada == 'g'):
        linha3[0] = usuario
    if (jogada == 'h'):
        linha3[1] = usuario
    if (jogada == 'i'):
        linha3[2] = usuario


    return

def escreve_oponente(move):
    if (move == 'a'):
        linha1[0] = oponente
    if (move == 'b'):
        linha1[1] = oponente
    if (move == 'c'):
        linha1[2] = oponente
    if (move == 'd'):
        linha2[0] = oponente
    if (move == 'e'):
        linha2[1] = oponente
    if (move == 'f'):
        linha2[2] = oponente
    if (move == 'g'):
        linha3[0] = oponente
    if (move == 'h'):
        linha3[1] = oponente
    if (move == 'i'):
        linha3[2] = oponente
    return

def apaga(jogada, move):
    if (jogada == oponente):
        print("%s", linha1)

def verificacao(linha1, linha2, linha3):
    if ((linha1[0] == " ") or (linha1[1] == " ") or (linha1[2] == " ") or (linha2[0] == " ") or (linha2[1] == " ") or (
        linha2[2] == " ") or (linha3[0] == " ") or (linha3[1] == " ") or (linha3[2] == " ")):
        resultado = False
    return resultado


print("Bem vindo ao jogo da velha!")
usuario = input("Voce gostaria de jogar com X ou O? \n")
usuario = usuario.upper()
if (usuario.upper() == 'X'):
    oponente = 'O'

else:
    oponente = 'X'

print("Voce vai jogar com", usuario)

print("Oponente joga com", oponente)
print("\n")

linha1 = [" ", " ", " "]
linha2 = [" ", " ", " "]
linha3 = [" ", " ", " "]
atualizatela(linha1, linha2, linha3)
cont = 0

while (verificacao(linha1, linha2, linha3) == False):
    jogada = input("Proximo movimento\n")
    escreve_usuario(jogada)
    atualizatela(linha1, linha2, linha3)
    cont += 1
    mirror(placar1, placar2, placar3)
    if (vitoria(placar1, placar2, placar3) == False):
        break;
    if (verificacao(linha1, linha2, linha3) == True):
        break;

    move = input("Movimento oponente\n")
    escreve_oponente(move)
    atualizatela(linha1, linha2, linha3)
    cont += 1
    mirror(placar1, placar2, placar3)
    if (vitoria(placar1, placar2, placar3) == False):
        break;
    if (verificacao(linha1, linha2, linha3) == True):
        break;

