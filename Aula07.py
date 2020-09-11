#Exercícios da aula 07
'''
def apresentarInterface():
    """Esta função apresenta a interface"""
    print('Este programa realiza a aquisição de dados para análise cinemática')
    print('digite 1 para acessar a área de análise de dados, 2 para continuar...')

apresentarInterface()
apresentarInterface()
apresentarInterface()

def somaDeListas(lista1,lista2):
    """Essa função soma duas listas"""
    for elementos in zip(lista1,range(0,len(lista1))):
        lista2[elementos[1]] = lista2[elementos[1]] + elementos[0]
    return lista2

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
print(somaDeListas(lista1,lista2))
print(somaDeListas.__doc__)

def lerlista():
    lista = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10):
        lista[i] = float(input('Digite 10 elementos para lista \n'))
    return lista

print(lerlista())

def arbitrary(x,y,*restanteDasVariaveis):
    print(x+y)
    print(restanteDasVariaveis)

arbitrary(2,4,"Gilberto Martins",2,3,4)


def lerlista(lista = [0,0,0,0,0,0,0,0,0,0]):
    
    return lista

print(lerlista())


def recursao(k):
    if(k > 0):
        resultado = k+recursao(k-1)
        print(resultado)
    else:
        resultado=0
    return resultado

recursao(10)


cube = lambda x: x*x*x

print(cube(2))
'''

class Point:
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY

    def getPointValue(self):
        return [self.x, self.y]

    def hipo(self):
        return (self.x**2 + self.y**2)**0.5
    
    def half(self, target):
        return (self.x+target.x)/2 + (self.y+target.y)/2

a = Point(34,85)
b = Point(3,9)

print(a.getPointValue())
print(a.hipo())
print(a.half(b))