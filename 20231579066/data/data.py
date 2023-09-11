import pandas as pd     # Se importa la libreria pandas, para el analisis de datos

# Importar datos del csv
data_teorico = pd.read_csv(r"C:\Users\USUARIO\OneDrive - Universidad Distrital Francisco José de Caldas\Programación II\Semana 5°\20231579066\data\Data ingeniero.csv")    # Se define la variable donde se llama a la tabla de datos

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico():     # Se define la función que contendra los datos teóricos
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]']   # Se define la variable que contendra el esfuerzo
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]']   # Se define la variable que contendra la deformación
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion   # Se devuelven los valores de las variables


