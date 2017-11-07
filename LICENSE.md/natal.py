#Cadastro de vendedores
info = []
import random
n=0
resposta = True
while resposta == True:
    Name = raw_input("Qual o seu nome? ")
    info.append(Name)
    print ("O seu cadastro foi feito")
    resposta= raw_input("Voce deseja cadastrar mais um? ")
    if resposta=="yes":
        resposta=True
        n=n+1;
    else:
        resposta=False

def escolherpessoas(info):
    listpessoas=[info]
    aleatorio=random.randint(0,n)
    pessoaescolhida1=listpessoas[aletorio]
    listpessoas.pop(random)
    pessoaescolhida2=listapessoas[aletorio]
    print ("Pessoa1", pessoaescolhida1, "Pessoa2", pessoaescolhida2)
