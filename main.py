import csv


# Construimos el diccionario leyendo el "csv" y volcando la info en la variable TIPO_COMPROBANTE
TIPO_COMPROBANTE = {}
with open('TABLACOMPROBANTES.csv', newline='') as input_file:
    csvreader = csv.reader(input_file, delimiter=';', quotechar='"')
    for row in csvreader:
        try:
            key = int(row[0])
        except ValueError:
            key = 0
        TIPO_COMPROBANTE[key] = row[1]
        
# En la rutina anterior mandamos al key "0" a todas las filas espurias del 'csv'. Ahora lo eliminamos.
TIPO_COMPROBANTE.pop(0)
        
# Imprimimos el diccionario en 'output.py'
with open('output.py', 'wt', encoding='utf8') as output_file:
    output_file.writelines('TIPO_COMPROBANTE = '+str(TIPO_COMPROBANTE))


