#Cadastro de vendedores
info = {'Nome': "", 'IngressosRecebidos': "", 'Fase': ""} 
cadVendedores = []
resposta = True
while resposta == True: 
    Name = raw_input("Qual o seu nome? ")
    NIng = raw_input("Quantos ingressos voce recebeu? ")
    Fase = raw_input("Voce esta em qual fase? ")  
    info = {'Nome': Name, 'IngressosRecebidos': NIng, 'Fase': Fase} 
    cadVendedores.append(info.copy())
    print ("O seu cadastro foi feito")
    print cadVendedores
    resposta= raw_input("Voce deseja cadastrar mais um? ")
    if resposta=yes:
        resposta=True
    else:
        resposta=False
    
