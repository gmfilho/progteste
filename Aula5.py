'''
lista = []
print(lista)

lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]

print(lista)
novaLista = ['Nova lista', lista]
print(novaLista)

#Acesssando uma lista
string = lista[0]
print(string)
print(lista[1])

print(novaLista[0])
print(novaLista[1])
print(novaLista[1][1])
print(novaLista[1][2])


#função len
lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
novaLista = ['Gilberto', lista]
print(len(lista))
print(len(novaLista))
print(len(novaLista[1]))


#Operadores + e -
lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
novaLista = ['Gilberto', lista]
print(lista+lista)
print(len(lista+lista))
print(len(lista+[1]))

print(lista*3)


#Operador in
lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
print('Peixe' in lista)
if('Peixe' in lista):
    print('Existe a palavra Peixe como um dos elementos da lista')

#operador max, min, sum
listaDeNumeros = [56,5,75,8,2,96,6]
print(max(listaDeNumeros))
print(min(listaDeNumeros))
print(sum(listaDeNumeros)/len(listaDeNumeros))

#função

lista = ['o carro é vermelho', 'Peixe', 123, 1097.85, True ]
print(lista[-1])
print(lista[-2])
print(lista[-3])


#Operador append

livros = ['Java', 'Python', 'SqlServer', 'Delphy']
print(livros)
livros.append('Android')
print(livros)

#Operador insert e pop

livros.insert(0,'Oracle')
print(livros)

print(livros.pop())
print(livros)

livros.remove('SqlServer')
print(livros)

livros.sort()
print(livros)

#reverse inverte a ordem

numeros = [1,5,3,4,8,10,22,9]
numeros.sort()
numeros.reverse()
print(numeros)


lista = ['o carro é vermelho', 'Peixe','Peixe', 'Gilberto', 'Hera']
print(lista.count('Peixe'))
lista.remove('Peixe')
print(lista)


a = [81,82,83]
b = a
print(b is a)
b[1]=999
print(a)

a = [81,82,83]
b = [81,82,83]
print(b is a)
print(b == a)

lista = [10,20,30,40,50,60,70,80,90]
print(lista.index(60))
print(lista[1:6])

tupla = (1,2,3,4)
print(tupla)
tupla = (1,)
print(tupla)
tupla = ()
print(tupla)

tupla = ('Maria', 'João', 'Carlos', 'Gilberto', 'Hera')
print(tupla[0:3])
#tupla[0] = 'Ana'
'''

dadosCovid = {}
print(dadosCovid)
dadosCovid = dict()
print(dadosCovid)

dadosCovidCasosNovos = {'Brasil':[0,1,0,0,1,0,0,0,2,3,4], 'Nordeste':[0,0,0,4,3,2,4,5,0,2]}
print(dadosCovidCasosNovos)
print(dadosCovidCasosNovos['Brasil'])