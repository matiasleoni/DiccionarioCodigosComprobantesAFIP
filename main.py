import csv
import requests
import pandas as pd
import xlrd

from info import AFIP_URL

# We download xls file from AFIP
urlget = requests.get(AFIP_URL, allow_redirects=True)
file = open('TABLACOMPROBANTES.xls', 'wb')
file.write(urlget.content)
file.close()


# We convert the xls to text-csv using pandas
read_file = pd.read_excel ("TABLACOMPROBANTES.xls")
read_file= read_file.drop(index=[0,1])
read_file= read_file.astype({'Tipos de Comprobantes': 'int'})

read_file.to_csv ("TABLACOMPROBANTES.csv", index = None, header=False, sep=';')





# We build the dictionary by reading the "csv" and dumping the information into
#  the variable TIPO_COMPROBANTE.
TIPO_COMPROBANTE = {}
with open('TABLACOMPROBANTES.csv', newline='', encoding='utf8') as input_file:
    csvreader = csv.reader(input_file, delimiter=';', quotechar='"')
    for row in csvreader:
        try:
            key = int(row[0])
        except ValueError:
            key = 0
        TIPO_COMPROBANTE[key] = row[1]
        
# En la rutina anterior mandamos al key "0" a todas las filas espurias del 'csv'. Ahora lo eliminamos.
#TIPO_COMPROBANTE.pop(0)
        
# Imprimimos el diccionario en 'output.py'
with open('output.py', 'wt', encoding='utf8') as output_file:
    output_file.writelines('TIPO_COMPROBANTE = '+str(TIPO_COMPROBANTE))


