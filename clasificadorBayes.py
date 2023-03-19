import pandas as pd

class clasificadorBayes:
    def __init__(self, X, y):
        self.X, self.y = X, y
        self.N = len(self.X)
        self.dim = len(self.X[0])
        self.atributos = [[]for _ in range(self.dim)]
        self.salida = {} 
        self.data = []
        
        for i in range(len(self.X)):
            for j in range (self.dim):
                if not self.X[i][j] in self.atributos[j]:
                    self.atributos[j].append(self.X[i][j])
                    
                if not self.y[i] in self.salida.keys():
                    self.salida[self.y[i]] = 1
                else:
                    self.salida[self.y[i]] += 1
                self.data.append([self.X[i], self.y[i]])
    
    def clasificador(self, entrada):
        respuesta = None
        maximo = -1
        
        for y in self.salida.keys():
            prob = self.salida[y]/self.N
            
            for i in range (self.dim):
                casos = [X for X in self.data if x[0][i]==entrada[i] and X[1] == y]
                n = len(casos)
                prob *= n / self.N
            if prob > maximo:
                maximo = prob
                respuesta = y
        return respuesta

datos = pd.read_csv('Titanic.csv')
print(datos.head())
#El map es como un forich, permite recorrer la lista
#Lamnda permite crear una clase sin necesidad de especificarlo como "def class"
y = list(map(lambda v: 'yes' if v==1 else 'no', datos['Survived'].values))
X = datos[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].values

y_entrenamiento = y[:600]
y_prueba = y[600:]

X_entrenamiento = X[:600]
X_prueba = X[600:]

nbc = clasificadorBayes(X_entrenamiento, y_entrenamiento)
no_casos = len(y_prueba)

bien = 0
mal = 0

for i in range(no_casos):
    prediccion = nbc.clasificador(X_prueba[i])
    print(y_prueba[i] + '-----' + prediccion)
    if y_prueba[i] == prediccion:
        bien += 1
    else:
        mal += 1
print("Total de casos: ", no_casos)
print("Correctos: ", bien)
print("incorrectos: ", mal)
print("Eficacia: ", bien/no_casos*100, "%")









    