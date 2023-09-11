import matplotlib.pyplot as plt   # Se importa la función que sirve para generar y visualizar gráficas
import numpy as np   # Se importa la función numpy, para realizar cálculos



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):   # Se genera un gráfico que compara los datos reales con los datos teóricos
    
    
    plt.figure(figsize=(15, 6))   # Tamaño del gráfico
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)   # Grafica los datos reales
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red')   # Grafica los datos reales
    plt.xlabel('Esfuerzo [kN]')  # Establece la etiqueta
    plt.ylabel('Deformación [mm]')   # Establece la etiqueta
    plt.title('Gráfica 2: teórico versus real [ZOOM]')   # Establece el titulo
    plt.xlim(0, x_lim)  # Establece los límites del eje x
    plt.ylim(0, y_lim)  # Establece los límites del eje y
    plt.grid()   # Genera una grilla en el grafico
    plt.gca().invert_yaxis()   # Invierte el eje del grafico
    plt.show()  # Finalmente genera el grafico

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model):    # Se genera un gráfico que relaciona  la predicción con los datos teóricos y reales y un valor especifico
  plt.figure(figsize=(15, 6))   # Tamaño del gráfico
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)   # Grafica los datos teóricos
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')   # Grafica los datos reales
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')   # Genera el gráfico con la predicción en un rango de valores definido
  plt.scatter(	3000 , prediction, color='green')  # Traza el punto del valor especifico a predecir
  plt.xlabel('Esfuerzo [kN]')   # Establece la etiqueta en x
  plt.ylabel('Deformación [mm]')   # Establece la etiqueta en y
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN')   # Establece el titulo del gráfico
  plt.xlim(0, 3000)   # Limita la visualización en el eje x
  plt.ylim(0, 45)   # Limita la visualización en el eje y
  plt.grid()   # Genera una grilla en el grafico
  plt.gca().invert_yaxis()   # Invierte el eje del grafico
  plt.show()   # Finalmente genera el grafico

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion):   # Genera la gráfica sin predicción
  plt.figure(figsize=(15, 6))    # Tamaño del gráfico
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion)    # Grafica los datos teóricos
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red')   # Grafica los datos reales
  plt.xlabel('Esfuerzo [kN]')    # Establece la etiqueta en x
  plt.ylabel('Deformación [mm]')    # Establece la etiqueta en y
  plt.title('Gráfica 1: teórico versus real')   # Establece el titulo del gráfico
  plt.grid()    # Genera una grilla en el grafico
  plt.gca().invert_yaxis()   # Invierte el eje del grafico
  plt.show()    # Finalmente genera el grafico
