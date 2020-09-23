#1º Modo

import random
import math
import time

class Eletrodos:
    ''' Classe utilizada para gerar a entrada dos eletrodos da Atividade Contextualizada 07 '''

  def __init__(self):
    #self.num = int(input('Informe o número de eletrodos fixados: '))
    self.num = 32
    arquivo = open('leituraEletrodos.txt', 'w')
    arquivo.close()
    self.leitura()

  def leitura(self):
    lista = list()
    for j in range(self.num):
      lista.append(random.randint(0,255))
    self.dados = lista
    self.armazenaEmArquivo()
    print('\nLeitura dos eletrodos realizada.')

  def armazenaEmArquivo(self):
    arquivo = open('leituraEletrodos.txt', 'r')
    conteudo = arquivo.readlines()
    conteudo.append('\nLeitura: '+str(self.dados))
    arquivo = open('leituraEletrodos.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()


class Dispositivo:
    ''' Classe que criar um dispositivo utilizado na Atividade Contextualizada 07 '''

  def __init__(self, entradaEletrodos, tempo):
    print('\nConfigurando Dipositivo:')
    self.entrada = entradaEletrodos.dados
    self.ledRGB = dict()
    self.ledRGB['R'] = self.configRGB('Vermelho', tempo)
    self.ledRGB['G'] = self.configRGB('Verde', tempo)
    self.ledRGB['B'] = self.configRGB('Azul', tempo)
    print('Dipositivo criado e eletrodos conectados ao dispositivo.')

  def configRGB(self, cor,tempoExperimento):
    tempoExperimento = int(tempoExperimento)
    saida = list()
    saida = [0.0]*tempoExperimento
    num = int(input('\nInforme quantas vezes o RGB('+ str(cor)+ ')irá acender: '))
    for i in range(num):
      tempoInicial = int(input('\nApós iniciado o experimento, informe com quantos segundos o RGB('+ str(cor) +') irá acender ['+str(i+1)+' de '+str(num)+']: '))
      duracao = int(input('Informe quantos segundos o RGB('+ str(cor) +') irá permanecer aceso: '))
      tempoFinal = tempoInicial + duracao
      if tempoFinal > tempoExperimento: tempoFinal = tempoExperimento
      w = float(input('De 0 a 1, informe a potência que o led irá acender nesse período: '))
      for i in range(tempoExperimento):
        if tempoInicial<=i<tempoFinal: saida[i] = w
      print('Saida PWM: ',saida)
    return saida

  def lerEletrodos(self, entradaEletrodos):
    self.entrada = entradaEletrodos.dados


class Experimento:

  def __init__(self):
    print('Iniciando novo experimento...')
    self.eletrodos = Eletrodos()
    self.tempoLimite = float(input('Informe o tempo do experimento: '))
    #self.tempoLimite = 2
    self.numDispositivos = int(input('Informe quantos dispositivos terão no experimento: '))
    self.listaDispositivos = self.criaDispositivos(self.tempoLimite)

  def dispositivosLeemEletrodos(self):
    for dispositivo in self.listaDispositivos:
      dispositivo.lerEletrodos(self.eletrodos)
    #return dispositivos

  def criaDispositivos(self, tempo):
    lista = list()
    for i in range(self.numDispositivos):
      lista.append(Dispositivo(self.eletrodos, tempo))
    return lista

  def execucao(self, passo):

    if(passo <= self.tempoLimite):
      i = 0
      for dispositivo in self.listaDispositivos:
        print('\nDISPOSITIVO ',i+1)
        print('ledRGB(Vermelho):',dispositivo.ledRGB['R'][passo])
        print('ledRGB(Verde):', dispositivo.ledRGB['G'][passo])
        print('ledRGB(Azul):', dispositivo.ledRGB['B'][passo])
        i+= 1
      self.eletrodos.leitura()


from os import system
import math
import time
import keyboard
from biblioteca07 import Dispositivo
from biblioteca07 import Eletrodos
from biblioteca07 import Experimento

system('clear')
experimento = list()
experimentoInicio = list()
experimentoTempo = list()

numExperimentos = int(input('Informe o número de experimentos: '))
for i in range(numExperimentos):
    print('\nEXPERIMENTO ', i+1)
    experimento.append(Experimento())
    experimentoInicio.append(int(input('Informe o tempo de inicio que esse experimento irá começar: ')))
    experimentoTempo.append(0)

tempoGlobal = 0
divisor = 1000
print('INICIANDO EXECUÇÃO DO EXPERIMENTO.')
while(True):
    print('#'*70)
    print('\nTEMPO DESDE A GÊNESE: ', tempoGlobal, ' segundos.')
    print("Caso aconteça algo errado, pressione 'a'.")
    for i in range(numExperimentos):
        if tempoGlobal >= experimentoInicio[i]:
            print('_'*50)
            print('EXPERIMENTO[',i+1,']:')
            experimento[i].execucao(experimentoTempo[i])
            experimentoTempo[i] += 1
    tempoGlobal += 1

    for i in range(divisor):
        time.sleep(1/divisor)
        if(keyboard.is_pressed('a')):
            print('Interrupção gerada. Saindo do programa...')
            break

#2º Modo 

from threading import Thread
import time
import random

class Dispositivo:
    def __init__(self,duracao,tempoON, intensity_r, intensity_g, intensity_b, tensaoeletrodo):
        self.duracao=duracao
        self.tempoON=tempoON
        self.intensity_r= intensity_r
        self.intensity_g= intensity_g
        self.intensity_b= intensity_b
        self.tensaoeletrodo= tensaoeletrodo

    def Luzes(self, disp):
        end_time = time.time() + self.duracao
        luz= ["vermelha", "verde", "azul"]
        while time.time() < end_time:
            print(disp, "-------Luz ", luz[random.randint(0,2)], " acesa\n")
            time.sleep(self.tempoON)
print('*******AVISO!**********')      
print("Em caso de emergencia, clique ctrl+c para parar o experimento!")
            
duracao= float(input("Qual a duração do experimento?"))
tempoON= float(input("Qual o tempo que a luz permanece ligada?"))
intensity_r= float(input(" Qual a itensidade da luz vermelha?"))
intensity_g= float(input(" Qual a itensidade da luz verde?"))
intensity_b= float(input(" Qual a itensidade da luz azul?"))
tensaoeletrodo=[]
for i in range(34):
    tensaoeletrodo.append(float(input("Qual a amplitude de tensão da matriz de 34 eletrodos?")))

parametros= Dispositivo(duracao, tempoON, intensity_r, intensity_g, intensity_b, tensaoeletrodo)

dispositivo1 = Thread(target=parametros.Luzes,args=["dispositivo 1"])
dispositivo2 = Thread(target=parametros.Luzes,args=["dispositivo 2"])

dispositivo1.start()
dispositivo2.start()

#3º Modo
nb_bits = 8

class optogenetic_matrix():
  
  def __init__(self, nb_leds = 32, name  = ''):
    """Inicializa matriz de eletrodos"""
    self.name = name
    
    # começa desligado
    self.dict_leds = {}
    self.leds_sequence = {}
    self.dict_leds['R'] = [0]*nb_leds
    self.dict_leds['G'] = [0]*nb_leds
    self.dict_leds['B'] = [0]*nb_leds
    
    # variáveis de sequência de ativação
    self.leds_sequence['time'] = []
    self.leds_sequence['R'] = []
    self.leds_sequence['G'] = []
    self.leds_sequence['B'] = []
    
    self.nb_leds = nb_leds
    print('Matriz instanciada com', self.nb_leds, 'LEDs RGB')
    
  def show_info(self):
    """Mostra informação completa do estado da matriz de eletrodos"""
    print('Mostrando os valores da matriz', self.name)    
    print('Valores R:', self.dict_leds['R'])
    print('Valores G:', self.dict_leds['G'])
    print('Valores B:', self.dict_leds['B'])
    print('Número de LEDs:', self.nb_leds)
    print('')
    
  def show_state(self): 
    """Mostra apenas valor atual dos LEDs da mtriz"""
    print('Valores R:', self.dict_leds['R'])
    print('Valores G:', self.dict_leds['G'])
    print('Valores B:', self.dict_leds['B'])    

  # Getters
  def get_name(self):
    """Retorna o nome dado à matriz"""
    return self.name
  
  def get_values_leds(self):
    """Retorna o dicionário de estado dos LEDs"""
    return self.dict_leds
  
  def get_nb_leds(self):
    """Retorna o número de LEDs da matriz"""
    return self.nb_leds
  
  def get_timing_sequence_value(self):
    """Retorna o momento seguinte de ativação dos LEDs"""
    if self.leds_sequence['time']:
      return self.leds_sequence['time'].pop(0)
    else:
      return float('NaN')
    
  def get_leds_sequence_value(self):
    """Retorna o estado seguinte de ativação dos LEDs"""
    if self.leds_sequence['R']:
      return self.leds_sequence['R'].pop(0),self.leds_sequence['G'].pop(0),self.leds_sequence['B'].pop(0)
    else:
      return float('NaN')
  
  # Setters
  def set_name(self, name):
    """Altera o nome dado à matriz"""
    self.name = name
  
  def stop_leds(self):
    """Zera os valores RGB dos LEDs da matriz"""    
    # desliga todos os leds
    self.dict_leds['R'] = [0]*self.nb_leds
    self.dict_leds['G'] = [0]*self.nb_leds
    self.dict_leds['B'] = [0]*self.nb_leds
    
  def set_values_leds(self, R, G, B):
    """Substitui os valores RGB dos LEDs da matriz por R, G  e B"""
    self.dict_leds['R'] = R
    self.dict_leds['G'] = G
    self.dict_leds['B'] = B
    
  def add_timed_values(self, led_values_R,led_values_G,led_values_B):
    """Inclui novo estado RGB na sequência de ativação"""
    self.leds_sequence['R'].append(led_values_R)
    self.leds_sequence['G'].append(led_values_G)
    self.leds_sequence['B'].append(led_values_B)  
    
  def set_values_single_led(self, led_index, value_R, value_G, value_B):
    """Altera o valor RGB de apenas um LED"""
    if(led_index >= self.nb_leds):
      print('Índice de LED não utilizável')
      print('Use um índice de 0 a', self.nb_leds)
    elif(value_R > 2**nb_bits - 1 or value_G > 2**nb_bits - 1 or value_B > 2**nb_bits - 1 ):
      print('Algum dos valores de RGB está acima do possível')
      print('Use valores individuais de 0 a', 2**nb_bits)
      print('Nenhum valor será alterado')
    else:
      self.dict_leds['R'][led_index] = value_R
      self.dict_leds['G'][led_index] = value_G
      self.dict_leds['B'][led_index] = value_B