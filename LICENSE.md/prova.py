print("Bem Vindo!")
print("")
estoque = open("estoque.txt", "r+")
a = estoque.read(9);
print "Produto1:", a
b = estoque.read(3);
print "Valor1:", b
c = estoque.read(9);
print "Produto2:", c
d = estoque.read(3);
print "Valor2:", d
e = estoque.read(9);
print "Produto3:", e
f = estoque.read(3);
print "Valor3:", f
g = estoque.read(9);
print "Produto4:", g
h = estoque.read(3);
print "Valor4:", h
i = estoque.read(9);
print "Produto5:", i
j = estoque.read(3);
print "Valor5:", j
produto = [a,c,e,g,i]
valor = [b,d,f,h,]
usuario = int(input("Quantos produtos diferentes voce quer comprar?"))
i = 1

while(i <= usuario):
    n=(input("Numero do Produto %i :" %i))
    print(produto[n])
    a=(input("Quantidade do Produto %i :" %i))
    print(int(valor[n])*a)
    i += 1


    
    

    
