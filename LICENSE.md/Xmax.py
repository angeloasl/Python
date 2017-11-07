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

while resposta == False:
    info2 = info
    listpessoas = info
    listpessoas2 = info2
    aleatorio=random.randint(0,n)
    pessoaescolhida1=listpessoas[aleatorio]
    listpessoas.pop(aleatorio)
    pessoaescolhida2=listpessoas[aleatorio]
    print ("Pessoa1", pessoaescolhida1, "Pessoa2", pessoaescolhida2)
    aleatorio2=random.randint(0,n)
    pessoaescolhida3=listpessoas2[aleatorio2]
    listpessoas2.pop(aleatorio2)
    pessoaescolhida4=listpessoas2[aleatorio2]
    print ("Pessoa3", pessoaescolhida1, "Pessoa4", pessoaescolhida2)
    n = n-2

