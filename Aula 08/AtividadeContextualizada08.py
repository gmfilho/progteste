#Atividade contextualizada 08

import csv 
#dadosC = dadosW 
def calculoAngulo(dadosC, dadosB):
    M = 0.98
    dt = 0.05
    angulo = 0
    angulo = M * (angulo + dadosC * dt) + (1 - M) * (dadosB)
    return angulo

def salvarAngulos(angulosa1, angulosa2)
    with open('AnguloCalculado.csv', 'w', newline= '') as csvFile:
        angwriter = csv.writer(csvFile, delimiter=' ', 
                                quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        angwriter.writerow(['Angulos calculados a partir do A1: \n'] + [angulosa1])
        angwriter.writerow(['Angulos calculados a partir do A2: \n'] + [angulosa2])
    with open('AnguloCalculado.txt', 'w') as arquivo:
        arquivo.write('Angulos calculados a partir do A1: \n')
        arquivo.write(str(angulosa1))
        arquivo.write('Angulos calculados a partir do A2: \n')
        arquivo.write(str(angulosa2))

a1=[]
a2=[]
filePath = 'coletaFlexJoelho.csv'

with open(filePath, 'r')