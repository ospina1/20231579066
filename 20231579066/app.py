from data.data import *   # Importa todo del módulo data.data
from BD.baseDatos import *     # Importa todo del módulo base de datos
from sklearn.linear_model import LinearRegression    # Importa la función de la biblioteca
from grafica.grafica import *    # Importa todo del módulo grafica
import pandas as pd     # Importa la libreria pandas

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()    # Se asigna los valores del data teorico a dos variables

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos()    # Se define una variable, la cual llama a la función lectura de datos
data_real = pd.DataFrame(data_list)    # Se crea un dataframe
data_real_fit = data_real     # Se crea una copia del data real
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1)   # Se extraen los valores y se almacenan en la variable x
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1)     # Se extraen los valores y se almacenan en la variable y
x_lim = data_real['Esfuerzo[kN]'].iloc[-1]     # Se determina el limite, a partir del valor maximo
y_lim = data_real['Deformacion[mm]'].iloc[-1]     # Se determina el limite, a partir del valor maximo
model = LinearRegression()    # Se crea un modelo de regresión
model.fit(X, y)    # Se ajusta el modelo
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)    # Se realiza una predicción utilizando el modelo ajustado para un valor de entrada de 3000 kN.
print('la predicción a 1000 kN es de: ', prediction ,'mm')     # Se muestra en pantalla la predicción


dataRealEsfuerzo = data_real['Esfuerzo[kN]']     # Se extraen los valores de esfuerzo y se almacenan en la variable
dataRealDeformacion = data_real['Deformacion[mm]']    # Se extraen los valores de deformación y se almacenan en la variable

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)      # Organizan y comparan los datos en las tres graficas
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)

