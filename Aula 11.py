'''
v = a.split("], '[")

v1 = v[0].split("[")[1]
print(v1)
for item in v1.split(',')
    teste = float(item)


a = a + h*derivada 

realizar um for para o movimento angular

a = 0 

for 
a = a + 0.05*0.061

class dispositivo:
    def __init__
        eletrodos = [0, 1, 2...]
        rbg = [r,g,b]
    def lerEletrodo(item)
        eletrodo[item] = input()
    def determinarcordoled(lista):
        rgb = lista
        print(lista)

a = dispositivo 

b = dispositivo

c = dispositivo 

lista = list()
for
    lista[0] = a.leeletrodo()
    lista[1] = a.leeletrodo()
    delay(0.05)

[1,2,3,4 0
 1,2,3,4 0,05
 1,2,3,4 0.1s
 1,2,3,4] 0.15s
delay



from sklearn.svm import SVC
from sklearn.multiclass import OneVsOneClassifier
#from sklearn.preprocessing import label_binarize

X = [[1,2], [2,4], [4,5] [3,2], [3,1]]
y = [0, 0, 1, 1, 2]

classif = OneVsOneClassifier(estimator = SVC(gamma='scale', random_state=0))

modeloTreinado = classif.fit(X,y)
print(modeloTreinado.predict(X))

X = [[1,3], [1,4], [3,5], [2,2], [4,1]]
print(modeloTreinado.predict(X))


from sklearn import svm
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt 

digits = load_digits()
#print(digits.data.shape)

#plt.gray()
#for images in digits.images:
#    plt.matshow(image)
#    plt.show()

clf = svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1],digits.target[:-1])
predicted = clf.predict(digits.data[-1:])
print(predicted)

images_and_predictions = list(zip(digits.images[-1:],predicted))
for index, (image,prediction) in enumerate(images_and_predictions[:1]):
    plt.axis('off')
    plt.imshow(image,cmap=plt.gray_r,interpolation='nearest')

plt.show()

'''

from skimage import data, io, filters
from skimage.io import imshow, show

imagem = data.coins()
io.imshow(imagem)
io.show()

edges = filters.sobel(imagem)
imshow(edges)
show()