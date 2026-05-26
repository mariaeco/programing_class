# ESCREVER A SOMA DE 1 A 15

#FOR POR VALOR
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
soma = 0
for numero in lista:
    print(soma, "+", numero, "=" )
    soma += numero
    print("     ", soma)


#FOR POR INDICE
soma = 0
ninicial = 1
nfinal = 15
for i in range(ninicial, nfinal+1): # para i de 1 a n-1 (16-1 =  15)
    print(soma, "+", i, "=" )
    soma += i
    print("     ", soma)