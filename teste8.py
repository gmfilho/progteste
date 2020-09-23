#1º IMC
'''
def calculoIMC(peso, altura):
    imc= peso/ (altura**2)
    return imc
def apresentarIMC(imc):

    if (imc<17):
        filecsv.write("Você está muito abaixo do peso, IMC\n")
    elif(imc>= 17 and imc <18.5):
        filecsv.write("Você está abaixo do peso normal, IMC\n ")
    elif(imc>= 18.5 and imc < 25):
        filecsv.write("Você está dentro do peso normal, IMC\n")
    elif(imc>= 25 and imc < 30):
        filecsv.write("Você está acima do peso normal, IMC\n")
    elif(imc>30):
        filecsv.write("Você está muito acima do peso, IMC\n")

deseja= 1
while(deseja==1):
    peso=float(input("Digite seu peso:"))
    altura=float(input("Digite sua altura:"))

    imc= calculoIMC(peso,altura)
    apresentarIMC(imc)
    deseja = int(input("Deseja calcular o seu imc novamente?")) 
    arquivo= int(input("Como deseja salvar os seus dados?( 1 para txt, 2 para csv)"))
filecsv.close()
'''

#2º 

import csv
def CalculoAngulo(dadow, dadoa):
    M=0.98
    dt=0.05
    ang=0
    ang= M *(ang + dadow * dt) + (1- M) * (dadoa)
    return ang
    
def SalvarAngulos(angulos_s1, angulos_s2):
    with open('anguloProcessado.csv', 'w', newline= '') as csvFile:
        spamWriter= csv.writer(csvFile, delimiter= ' ',
        quotechar ='|', quoting= csv.QUOTE_MINIMAL)

        spamWriter.writerow(["Angulos calculados para o sensor 1:\n"]+[angulos_s1]) 
        spamWriter.writerow(["Angulos calculados para o sensor 2:\n"]+[angulos_s2])
    with open('anguloProcessado.txt', 'w') as fileObject:
        fileObject.write("Angulos calculados para o sensor 1:\n")
        fileObject.write(str(angulos_s1)) 
        fileObject.write("Angulos calculados para o sensor 2:\n")
        fileObject.write(str(angulos_s2))
          

s1=[]
s2=[]
filePath= 'coletaFlexJoelho.csv'
with open(filePath, 'r') as fileObject:
    for line in fileObject:
        dadosSensor= line.split('],""[')
        sensor1 = dadosSensor[0].split('[')[1]
        sensor2 = dadosSensor[1][:-5]
        
        for dadosSensor1 in sensor1.split(','):
            s1.append(float(dadosSensor1))
        for dadosSensor2 in sensor2.split(','):
            s2.append(float(dadosSensor2))
    

    n = 2000
    splited1 = []
    splited2 = []
    angulos_s1= []
    angulos_s2= []
    len_l = len(s1)
    for i in range(n):
        start = int(i*len_l/n)
        end = int((i+1)*len_l/n)
        splited1.append(s1[start:end])
        splited2.append(s2[start:end])
        angulos_s1.append(CalculoAngulo(splited1[i][4], splited1[i][1]))
        angulos_s2.append(CalculoAngulo(splited2[i][4], splited2[i][1]))
         
    SalvarAngulos(angulos_s1, angulos_s2)

