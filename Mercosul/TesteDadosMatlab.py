import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import scipy.io


path_images = 'C:\\Users\\gilbe\\Documents\\Projeto_Mercosul2020\\(Erika) Dados EEG\\Imagens\\'
path_data = 'C:\\Users\\gilbe\\Documents\\Projeto_Mercosul2020\\(Erika) Dados EEG\\'

mat = scipy.io.loadmat(path_data + 'EEG-teste1.mat')
mat2 = scipy.io.loadmat(path_data + 'EEG-teste2.mat')

#mat2.keys()
#print(mat2.keys())

#dict_keys(['__header__', '__version__', '__globals__', 'ch1', 'ch2', 'ch3', 'ch4', 'ch6', 'ch5', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11', 'ch12', 'time'])

'''
plt.plot(mat2['time'].T[50:500], mat2['ch1'][0][50:500])
plt.show()
'''

plt.plot(mat2['time'].T[50:500], mat2['ch5'][0][50:500])
plt.show()

