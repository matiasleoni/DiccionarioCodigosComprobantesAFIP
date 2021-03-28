# Diccionario de tipos de comprobante AFIP en formato Python

## Diccionario para uso libre:

Este es un diccionario en formato Python con los códigos de tipo de comprobante de AFIP y su descripción. Los interesados pueden obtener directamente el diccionario con el formato
```
{1:'FACTURAS A',2:'NOTAS DE DEBITO A',3:'NOTAS DE CREDITO A'....}
```
en el archivo *output.py*. Son un total de 96 entradas.

## Código para generar el diccionario 

Aquellos interesados en reutilizar el código en el caso de futuros cambios en AFIP, se contruyó el archivo *output.py* de la siguiente manera: 
1. El archivo en formato Excel *TABLACOMPROBANTES.xls* fue descargado del sitio de AFIP http://www.afip.gov.ar/fe/documentos/tablas%20generales%20v.0.1%20%2026012011.xls
2. Luego lo exporté como archivo de texto (comma separated values) *TABLACOMPROBANTES.csv*.
3. Corriendo el script *main.py* se genera el diccionario de códigos y se vuelca el resultado en la variable TIPO_COMPROBANTE y en el archivo *output.py*
