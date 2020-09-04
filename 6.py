#Atividade Contextualizada - Aula 06

#Programa para cirurgia estereotáxica em animais 

# Primeiro vamos definir as variáveis

#Variáveis para posição do animal 

posicao = list()
parafusos = 0 
posicaoParafusos = list()
resp = ''

#Posições das agulhas (Valores em cm)

#Uso do dicionário
posicionamentoAgulhas = {'AP': 6.42, 'LL1': -3.23, 'LL2': 3.23, 'DV': 4.2}
#Uso da Tupla
posicoesdasAgulhas = ('AP', 'LL1', 'LL2', 'DV')
#Uso da lista
hipo = [-0.42, -0.3, 0.3, -0.2] 
animal = dict()
anestesia = dict()

#Início do programa

print('Bem-vindo(a) ao programa de cirurgia estereotáxica em animais.')
print('')
print('Este programa irá automatizar e auxiliar no procedimento cirúrgico.\n', 'Por favor, responda todas as perguntas da forma que são solicitdas. \n')

resp = input('Vamos começar a operação? Responda ''sim'' para continuar.\n')

while (resp != 'sim'):
    resp = input('Quando estiver pronto, digite "sim" para continuar.\n')

print('O programa foi iniciado e iremos continuar com a operação.')

#Primeira Etapa:

resp = ''

while (resp != 'sim'):
    anestesia['peso'] = float(input('Qual o peso do animal em gramas?\n'))
    anestesia['nome'] = input('Qual será o fármaco utilizado?\n')
    anestesia['quant'] = float(input('Qual a quantidade em ml?\n'))
    resp = input('Digite "sim" caso os parâmetros estejam corretos: \nPeso: %s \nFármaco: %s\nQuantidade em ml:%s' %(farmacoAnestesia['peso'], farmacoAnestesia['nome'], farmacoAnestesia['quant'])
    if (resp != 'sim'):
        print('Verifique e informe os parâmetros novamente.')