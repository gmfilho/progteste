#Atvc8

'''
import csv
def ler():
     with open('C:\Users\Win-7\Documents\GitHub\ProgISD20202\Dayana Vieira\Aula 8\coletaFlexJoelho.csv','r') as fileObject:
             lista=[]
             for line in fileObject:
               dadosEsp=line.split('],""[')
               esp2=dadosEsp[1].split(']""')[0]
               #print(esp2)
               esp1=dadosEsp[0].split("[")[1]
               #print(esp1)
               for dadosEsp1 in esp1.split(","):
                     #print(float(dadosEsp1))
                     lista.append(float(dadosEsp1)) 
               for dadosEsp2 in esp2.split(","):
                     #print(float(dadosEsp2))
                     lista.append(float(dadosEsp2)) 
     return lista
def AngleCalculate():
     coleta=ler()
     ang=0
     angulos=[]
     #conferencia=[]
     for i in range (4,len(coleta),4):
          #conferencia.append(coleta[i])
          ang=0.98*(ang+coleta[i]*0.05)+(1-0.98)*coleta[i-3]
          angulos.append(ang)
     return angulos
def salvando ():
     coleta=AngleCalculate()
     sensor1=[]
     sensor2=[]
     for i in  range(0,len(coleta),1):
          if ((i%2)==0):
               sensor1.append(coleta[i])
          else:
               sensor2.append(coleta[i])
     with open('anguloprocessado.csv', 'w', newline='') as csvfile:
          spamwriter = csv.writer(csvfile, delimiter= ' ',
                        quotechar= '|', quoting=csv.QUOTE_MINIMAL)
         
          spamwriter.writerow(['Valores dos Angulos'] )
          spamwriter.writerow(['Sensor 1: \n'] + [sensor1])
          spamwriter.writerow(['Sensor 2: \n']+[sensor2])
     with open('anguloprocessado.csv','r',newline='') as csvfile:
          spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
          for row in spamreader:
               print(','.join(row))
     with open('anguloprocessado.txt','w') as FileObject:
          FileObject.write("***Valores dos Angulos***\n#Sensor 1:\n")
          FileObject.writelines(str(sensor1))
          FileObject.write("\n\n#Sensor 2:\n")
          FileObject.writelines(str(sensor2))
     with open('anguloprocessado.txt','r') as FileObject:
          print(FileObject.read())

print("****Bem vindo à Calculadora de Angulo****")
salvando()

#Atvc 7 

import threading,time,os,webcolors,random,keyboard
from googletrans import Translator
from datetime import datetime
class Dispositivo (threading.Thread):
    def __init__(self,idExp,idt,TempoSessao,TempInicialON,TempoON,RGB_red,RGB_green,RGB_blue,eletrodos,language):
        threading.Thread.__init__(self)
        self.idExp=idExp
        self.idt=idt
        self.TempoSessao=TempoSessao
        self.TempInicialON=TempInicialON
        self.TempoON=TempoON
        self.RGB_red=RGB_red
        self.RGB_green=RGB_green
        self.RGB_blue=RGB_blue
        self.eletrodos=eletrodos
        self.language=language
    def run(self):
        tradutor=Translator()
        TXT=tradutor.translate("inicio da sessão:", dest=self.language)
        print(TXT.text+" %s" % ((self.idExp)+1))
        TXT=tradutor.translate("#Caso ocorram erros no experimento apertar a tecla 'esc'!", dest=self.language)
        print(TXT.text)
        procThread(self.idExp,self.idt,self.TempoSessao,self.TempInicialON,self.TempoON,self.RGB_red,self.RGB_green,self.RGB_blue,self.language)
        TXT=tradutor.translate("Termino da sessão: ", dest=self.language)
        print(TXT.text+"%s" % ((self.idExp)+1))

def procThread(idExp,idt,TempoSessao,TempoInicialON,TempoON,red,green,blue,lang):
    tradutor=Translator()
    RGB=webcolors.rgb_to_name((red,green,blue))
    Cor=tradutor.translate(RGB, dest=lang)
    Estimulo=tradutor.translate("Estímulo com led de coloração: ",dest=lang)
    temporizador=tradutor.translate("Time:",dest=lang)
    Desligada=tradutor.translate("Desligada!",dest=lang)
    Session=tradutor.translate("Dispositivo: ",dest=lang)
    experimento=tradutor.translate("**Experimento:",dest=lang)
    now=datetime.now()
    aux=int(now.second+TempoSessao.second)//60
    SegundoFinal=int(now.second+TempoSessao.second-(aux*60))
    SegundoAgora=int(now.second)
    minutoFinal=int(now.minute+TempoSessao.minute+aux)
    minutoAgora=int(now.minute)
    ligada=[]
    Sinal_eletrodo=[]
    for i in range(0,len(TempoInicialON)):
       aux=int(now.second+TempoInicialON[i].second)//60
       SegundoFinal_ligada=int(now.second+TempoInicialON[i].second-(aux*60))
       minutoFinal_ligada=int(now.minute+TempoInicialON[i].minute+aux)
       datatxt=str(minutoFinal_ligada)+':'+str(SegundoFinal_ligada)
       Tempo=datetime.strptime(datatxt,'%M:%S')
       ligada.append(Tempo)
  
    
    while((minutoAgora!=minutoFinal) or (SegundoAgora!=SegundoFinal)):
        if keyboard.is_pressed('esc'):
            TXT=tradutor.translate("Experimento encerrado:", dest=lang)
            print(TXT.text)
            break

        for j in ligada:
            if keyboard.is_pressed('esc'):
                TXT=tradutor.translate("Experimento encerrado:", dest=lang)
                print(TXT.text)
                break

            if((j.minute==minutoAgora)):
                for i in range (0,TempoON):
                    print("\r{6}:{7}.{4}:{5}. {2}:{0}. {3}:{1}".format(Cor.text,i,Estimulo.text,temporizador.text,Session.text,idt+1,experimento,idExp+1))
                    #os.system("cls")
                    for w in range (0,1000):
                        now=datetime.now()
                        SegundoAgora=now.second
                        minutoAgora=now.minute
                        if keyboard.is_pressed('esc'):
                            TXT=tradutor.translate("Experimento Encerrado:", dest=lang)
                            print(TXT.text)
                            break

                        #print("Entrando",minutoAgora,minutoFinal,SegundoAgora,SegundoFinal)
                        if ((minutoAgora==minutoFinal) and (SegundoAgora==SegundoFinal)):
                            break
                        else:
                            sinal=round(random.uniform(-500,500),6)
                            Sinal_eletrodo.append(sinal)
                        time.sleep(0.001)
                    """now=datetime.now()
                    SegundoAgora=now.second
                    minutoAgora=now.minute"""
            else:
                print("\r {3}:{4}. {0}:{1}.{2}".format(Session.text,idt+1,Desligada.text,experimento,idExp+1))
                #os.system("cls")
                for w in range (0,1000):
                        now=datetime.now()
                        SegundoAgora=now.second
                        minutoAgora=now.minute
                        if keyboard.is_pressed('esc'):
                            TXT=tradutor.translate("Experimento encerrado:", dest=lang)
                            print(TXT.text)
                            break
                        #print("Entrando",minutoAgora,minutoFinal,SegundoAgora,SegundoFinal)
                        if ((minutoAgora==minutoFinal) and (SegundoAgora==SegundoFinal)):
                            break
                        else:
                            sinal=round(random.uniform(-500,500),6)
                            Sinal_eletrodo.append(sinal)
                        time.sleep(0.001)
            """now=datetime.now()
            SegundoAgora=now.second
            minutoAgora=now.minute"""
        now=datetime.now()
        SegundoAgora=now.second
        minutoAgora=now.minute
    print(idExp,"Sinais recebidos",Sinal_eletrodo)

def StartThread():
    print("****Bem vindo ao Optogenetics Solution***")
    tradutor=Translator()
    Detector=input("#Para iniciar o sistema escreva 'Start the system' em sua lingua nativa: ")
    Lang=tradutor.detect(Detector)
    Txt=tradutor.translate('Digite a quantidade de Experimentos simultâneos: ', dest=Lang.lang)
    num=int(input(Txt.text))
    Dispositivos=[]
    for i in range(0,num,1):
        Exp=i
        Txt=tradutor.translate('***Informações do experimento {}: ***'.format(i+1), dest=Lang.lang)
        print(Txt.text)
        Txt=tradutor.translate('Entre com a quantidade de Dispositivos Utlizados no experimento {}:'.format(i+1), dest=Lang.lang)
        Num_Dispositivosint=int(input(Txt.text))
        Txt=tradutor.translate('Entre com o tempo (Minutos) de sessão do experimento {}): '.format(i+1), dest=Lang.lang)
        TempoSessaoTxt=input(Txt.text)
        TempoSessao=datetime.strptime(TempoSessaoTxt,'%M:%S')
        for j in range (0,Num_Dispositivosint,1):
            idt= j
            Txt=tradutor.translate('Entre com a quatidade de vezes que o dispositivo {} será ligado: '.format(j+1), dest=Lang.lang)
            qtd=int(input(Txt.text))
            Txt=tradutor.translate('Entre com  as 32 posições do dispositivo {}. Da seguinte forma 1,23,45,6,...:'.format(j+1), dest=Lang.lang)
            eletrodos=input(Txt.text)
            eletrodos=str(eletrodos).split(',')
            Txt=tradutor.translate('Entre com a quantidade de tempo em Segundos, que a luz deve permanecer ligada :', dest=Lang.lang)
            TempoON=int(input(Txt.text))
            TempoInicialON=[]
            for z in range(0,qtd,1):
                Txt=tradutor.translate('Digite em que tempo o dispositivo {0} será ligado na interação {1}. Ex. 0:30, isto é, após de 30 segundos que o dispositivo foi ligado:'.format(j+1,z+1), dest=Lang.lang)
                TempoInicialTxt=input(Txt.text)
                TempoInicialDT=datetime.strptime(TempoInicialTxt,'%M:%S')
                TempoInicialON.append(TempoInicialDT)     
            Txt=tradutor.translate('Entre com o Primeiro valor RGB (0 a 255):', dest=Lang.lang)
            RGB_red=int(input(Txt.text))
            Txt=tradutor.translate('Entre com o segundo valor RGB (0 a 255):', dest=Lang.lang)
            RGB_green=int(input(Txt.text))
            Txt=tradutor.translate('Entre com o Terceiro valor RGB (0 a 255):', dest=Lang.lang)
            RGB_blue=int(input(Txt.text))
            Dispositivos.append(Dispositivo(Exp,idt,TempoSessao,TempoInicialON,TempoON,RGB_red,RGB_green,RGB_blue,eletrodos,Lang.lang))
    for w in range (0,len(Dispositivos)):
        Dispositivos[w].start()
    for t in Dispositivos:
        t.join()    

#NovoModo 

from os import system
system('clear')
import csv
import math
sensor1 = list()
sensor2 = list()
variaveis = ('ax','ay','az','gx','gy','gz')
angulo = list()


def ang(sensor, angulo, M=0.98, dt=0.05):
  dadoa = (sensor['ax']/(sensor['ay']**2 + sensor['az']**2)*180/math.pi)
  #try:
  #  return M*(ang(sensor,angulo) + sensor['gy']*dt) + (1 - M)*dadoa
  #except:
  #  return M*(sensor['ay'] + sensor['gy']*dt) + (1 - M)*dadoa
  if len(angulo): return M*(angulo[-1] + sensor['gy']*dt) + (1 - M)*dadoa
  else: return M*(sensor['ax'] + sensor['gy']*dt) + (1 - M)*dadoa

with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
  spamreader = csv.reader(arquivo, delimiter="'", quotechar='|')

  j = 0
  for linha in spamreader:
    saida = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
    sensor1.append(dict())
    for i in range(len(saida)):
      sensor1[j][variaveis[i]] = float(saida[i])
    j+=1

arquivoTxt = open('anguloProcessado.txt','w')
arquivoCsv = open('anguloProcessado.csv', 'w', newline='')
spamwriter = csv.writer(arquivoCsv, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)

arquivoTxt.write('Sensor 1:\n')

for x in sensor1:
  angulo.append(ang(x,angulo))



for i in angulo:
  print(i)
  arquivoTxt.write(str(i))
  spamwriter.writerow(str(i))

print('Saidas geradas')
arquivoTxt.close()
arquivoCsv.close()

#########################################

import csv
M = 0.98
dt = 0.05

def init_dict_dados():
  """Cria a estrutura vazia que receberá os dados"""
  dict_dados = []
  dict_dados.append([])
  dict_dados.append([])
  dict_dados[0] = {}
  dict_dados[0]['ax'] = []
  dict_dados[0]['ay'] = []
  dict_dados[0]['az'] = []
  dict_dados[0]['wx'] = []
  dict_dados[0]['wy'] = []
  dict_dados[0]['wz'] = []
  dict_dados[1] = {}
  dict_dados[1]['ax'] = []
  dict_dados[1]['ay'] = []
  dict_dados[1]['az'] = []
  dict_dados[1]['wx'] = []
  dict_dados[1]['wy'] = []
  dict_dados[1]['wz'] = []
  return dict_dados

def list_to_dict(dados_lista, dict_dados):
  """Passa a lista de dados por linha pra estrutura"""
  dict_dados[0]['ax'].append(dados_lista[0])
  dict_dados[0]['ay'].append(dados_lista[1])
  dict_dados[0]['az'].append(dados_lista[2])
  dict_dados[0]['wx'].append(dados_lista[3])
  dict_dados[0]['wy'].append(dados_lista[4])
  dict_dados[0]['wz'].append(dados_lista[5])
  
  dict_dados[1]['ax'].append(dados_lista[6])
  dict_dados[1]['ay'].append(dados_lista[7])
  dict_dados[1]['az'].append(dados_lista[8])
  dict_dados[1]['wx'].append(dados_lista[9])
  dict_dados[1]['wy'].append(dados_lista[10]) 
  dict_dados[1]['wz'].append(dados_lista[11]) 
  
  return dict_dados

def calcula_angulo(ang, dado_w, dado_a):
  """ aplica a formula ang = M*(ang + dado_w*dt) + (1-M)*(dado_a)"""
  return M*(ang + dado_w*dt) + (1-M)*(dado_a)

def append_ang(dict_dados, ind_sensor):
  """Para cada linha de dados do sensor, calcula o angulo e concatena na estrutura"""
  angulo_sensor = dict_dados[ind_sensor]['ay'][0]
  for idado in range(len(dict_dados[ind_sensor]['ay'])):
    angulo_sensor = calcula_angulo(angulo_sensor, dict_dados[ind_sensor]['wy'][idado], \
                                   dict_dados[ind_sensor]['ay'][idado])
    dict_dados[ind_sensor]['angy'].append(angulo_sensor)
  return dict_dados

# inicia a estrutura de dados
dict_dados = init_dict_dados()

# Lendo um arquivo csv
with open('coletaFlexJoelho.csv', 'r', newline='') as csvfile:
  dados_flex_joelho = csv.reader(csvfile, delimiter='"')
  start_line = True
  
  for row in dados_flex_joelho:
    
    # primeira linha é diferente das outras
    if start_line:
      print(row)
      ind1 = 1
      ind2 = 2
      sensor1 = row[ind1].split(',') # separa em elementos
      sensor2 = row[ind2].split(',')

      sensor1.remove(sensor1[-1])
      dados_sensor1 = [float(x.replace('"', '').replace('[', '').replace(']','')) for x in sensor1]
      dados_sensor2 = [float(x.replace('"', '').replace('[', '').replace(']','')) for x in sensor1]
      dados_sensor1.extend(dados_sensor2)
      dados_sensores = dados_sensor1
      start_line = False
      
    # restante das linhas. Se quiser testar o erro, é só apagar do if start_line até esse else
    else:
      dados_sensores = row[0]
      dados_sensores = dados_sensores.split(',') # separa em elementos
      
      # substitui aspas e colchetes por nada e transforma lista de strings em lista de floats
      dados_sensores = [float(x.replace('"', '').replace('[', '').replace(']','')) for x in dados_sensores]
    
    # Insere dados na estrutura
    dict_dados = list_to_dict(dados_sensores, dict_dados)


# Os dados são acessíveis através de dict_dados
# dict_dados[0] é o sensor 1
# dict_dados[1] é o sensor 2
# cada sensor possui dados 'ax', 'ay', 'az', 'wx', 'wy', 'wz'
# ou seja, acessa todos os dados de um eixo por exemplo fazendo dict_dados[0]['ay']

dict_dados[0]['angy'] = []
dict_dados[1]['angy'] = []

dict_dados = append_ang(dict_dados, 0)
dict_dados = append_ang(dict_dados, 1)
    
# salva os valores calculados em arquivo csv
with open('anguloProcessado.csv','w',newline = '') as csvfile:
  ang_writer = csv.writer(csvfile, delimiter = ',')
  for ang_sensor1, ang_sensor2 in zip(dict_dados[0]['angy'],dict_dados[1]['angy']):
    ang_writer.writerow([str(ang_sensor1), str(ang_sensor2)])
    
# salva os valores calculados em arquivo txt
with open('anguloProcessado.txt','w',newline = '') as txtfile:
  for ang_sensor1, ang_sensor2 in zip(dict_dados[0]['angy'],dict_dados[1]['angy']):
    txtfile.write(str(ang_sensor1) + ',' + str(ang_sensor2) + '\n')

'''

########################################

from os import system
system('clear')
import csv
import math
import numpy as np
sensor1 = np.array([])
sensor2 = np.array([])
variaveis = ('ax','ay','az','gx','gy','gz')
angulo = np.array([])



def ang(sensor, angulo, M=0.98, dt=0.05):
  dadoa = (sensor[0]/(sensor[1]**2 + sensor[2]**2)*180/math.pi)
  #try:
  #  return M*(ang(sensor,angulo) + sensor['gy']*dt) + (1 - M)*dadoa
  #except:
  #  return M*(sensor['ay'] + sensor['gy']*dt) + (1 - M)*dadoa
  if len(angulo): return M*(angulo[-1] + sensor[4]*dt) + (1 - M)*dadoa
  else: return M*(sensor[0] + sensor[4]*dt) + (1 - M)*dadoa

with open('coletaFlexJoelho.csv', 'r', newline='') as arquivo:
  spamreader = csv.reader(arquivo, delimiter="'", quotechar='|')
  j = 0

  for linha in spamreader:
    saida = linha[0].split(',""')[0].split('"')[1].split('[')[1].split(']')[0].split(',')
    lista = list()
    for i in range(len(saida)):
      lista.append(float(saida[i]))
    lista = np.array(lista)
    if j == 0:
      sensor1 = np.array(lista)
    else: sensor1 = np.vstack((sensor1,lista))
    j+=1

arquivoTxt = open('anguloProcessado.txt','w')
arquivoCsv = open('anguloProcessado.csv', 'w', newline='')
spamwriter = csv.writer(arquivoCsv, delimiter = ' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)

arquivoTxt.write('Sensor 1:\n')

for x in sensor1:
  angulo = np.append(angulo, np.around(ang(x,angulo), decimals=2))

for i in angulo:
  #print(i)
  arquivoTxt.write(str(i))
  spamwriter.writerow(str(i))

print('Saidas geradas')
arquivoTxt.close()
arquivoCsv.close()


print('Somatório: ',np.around(angulo.sum(), decimals=2))
print('Média: ', np.around(angulo.mean(), decimals=2))
print('Angulo menor: ', np.around(angulo.min(), decimals=2))
print('Angulo maior: ', np.around(angulo.max(), decimals=2))
print('Integral: ', np.around(np.trapz(angulo), decimals=2))
print('Variancia: ', np.around(angulo.var(), decimals=2))
print('Diferença entre angulos: ', np.around(np.diff(angulo), decimals=2))

