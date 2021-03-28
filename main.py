import ast

# volcamos en la variable 'file_line_list' la lista de líneas en el archivo 'TABLACOMPROBANTES.csv'
with open('TABLACOMPROBANTES.csv', 'rt') as input_file:
    file_line_list=input_file.readlines()

def organizar_caracteres(file_line_list):
    '''
    INPUT: Lista de líneas contenidas en el archivo TABLACOMPROBANTES.csv
    OUTPUT: String con esas líneas con algunas sustituciones convenientes de caracteres
    '''
    # Unir los elementos de la lista en un único string
    file_string = ''.join(file_line_list)
    
    # Algunas descripciones de los códigos tienen "comas" que debemos reemplazar puesto que usaremos la
    # coma para separar elementos del diccionario. A su vez reemplazamos los saltos de línea por comas y
    # eliminamos las líneas espurias
    file_string = ((file_string.replace(',','-')).replace('\n',',')).replace(',;','')

    # Eliminamos los dos últimos caracteres y agregamos corchetes que definen al diccionario
    file_string = '{'+file_string[:len(file_string)-2]+'}'
    
    # Eliminamos los paréntesis de apertura y clausura reemplazandolos por guiones "-" (pues molestan  en
    # la conversión) y reemplazamos los caracteres de separación de campos ";" por ":", naturales en los
    # diccionarios de Python.
    file_string = ((file_string.replace('(','-')).replace(')', '-')).replace(';',':')
    return file_string

def encomillar_descripcion(file_string):
    '''
    INPUT: String acomodado por la función "organizar_caracteres()"
    OUTPUT: String definitivo con el diccionario
    '''
    # Esta operación identifica las descripciones de los códigos y las encomilla
    elem_num = file_string.count(':')
    pos_to_search_col = 1
    pos_to_search_coma = 1
    for colon in range(elem_num):
        location_col = file_string.find(':',pos_to_search_col)
        location_coma = file_string.find(',',pos_to_search_coma)
        
        encomillado = "'"+file_string[location_col+1:location_coma]+"'"
        file_string = file_string[:location_col+1]+encomillado+file_string[location_coma:]
        
        pos_to_search_col = location_col+1
        pos_to_search_coma = location_coma+3
    return file_string

# a partir de la lista obtenida del csv producimos la string que contiene el diccionario
file_string = organizar_caracteres(file_line_list)
file_string = encomillar_descripcion(file_string)


# Imprimimos el diccionario en 'output.py'
with open('output.py', 'wt', encoding='utf8') as output_file:
    output_file.writelines('TIPO_COMPROBANTE = '+file_string)
    
# Transformamos el string-diccionario "file_string" en un verdadero diccionario y lo volcamos en la
# variable TIPO_COMPROBANTE
TIPO_COMPROBANTE = ast.literal_eval(file_string)

