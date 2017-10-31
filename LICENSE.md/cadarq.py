#Cadastro de vendedores
info = {'Nome': "", 'IngressosRecebidos': "", 'Fase': ""} 
cadVendedores = []
resposta = True
def NameCaracteres(string)
    while (len(string)<10):
        Name = Name + ""
        Name = Name[:10]
        return Name
def NameCaracteres(string)
    while (len(string)<2):
        NIng = NIng + ""
        NIng = NIng[:2]
        return NIng
def NameCaracteres(string)
    while (len(string)<2):
        Fase = Fase + ""
        Fase = Fase[:2]
        return Fase
def NameCaracteres(string)
    while (len(string)<2):
        Age = Age + ""
        Age = Age[:2]
        return Age
    
    
while resposta == True: 
    cadastro= open ("arq.txt","a")
    Name = raw_input("Qual o seu nome? ")
    cadastro.write(Name)
    Age = raw_input("Voce tem quantos anos? ")
    cadastro.write(Age)
    NIng = raw_input("Quantos ingressos voce recebeu? ")
    cadastro.write(NIng)
    Fase = raw_input("Voce esta em qual fase? ")  
    cadastro.write(Fase)
    info = {'Nome': Name, 'IngressosRecebidos': NIng, 'Fase': Fase} 
    cadVendedores.append(info.copy())
    cadastro.close()
    print ("O seu cadastro foi feito")
    print cadVendedores
    resposta= raw_input("Voce deseja cadastrar mais um? ")
    if resposta=="Y":
        resposta=True
    else:
        resposta=False
