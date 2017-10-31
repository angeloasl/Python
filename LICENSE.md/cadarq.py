#Cadastro de vendedores
info = {'Nome': "", 'IngressosRecebidos': "", 'Fase': ""} 
cadVendedores = []
resposta = True
while resposta == True: 
    cadastro= open ("arq.txt","a")
    Name = raw_input("Qual o seu nome? ")
    cadastro.write(Name)
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
    
