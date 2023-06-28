# Diccionario de tipos de comprobante AFIP en formato Python

![alt text](https://github.com/matiasleoni/DiccionarioCodigosComprobantesAFIP/blob/main/portada.png?raw=true)

## Diccionario para uso libre:

Este es un diccionario en formato Python con los códigos de tipo de comprobante de AFIP y su descripción. Los interesados pueden obtener directamente el diccionario con el formato
```
{1:'FACTURAS A',2:'NOTAS DE DEBITO A',3:'NOTAS DE CREDITO A'....}
```
en el archivo *output.py*. Son un total de 96 entradas.

## Código para generar el diccionario 

Aquellos interesados en reutilizar el código en el caso de futuros cambios en AFIP, se construyó el archivo *output.py* de la siguiente manera: 
1. La rutina *main.py* descarga el Excel *TABLACOMPROBANTES.xls* del sitio de AFIP <https://www.afip.gob.ar/fe/documentos/TABLACOMPROBANTES.xls> (última consulta 28/6/2023). Si esta dirección falla, basta poner la nueva dirección en el archivo *info.py*.
2. Luego lo convierte en un CSV *TABLACOMPROBANTES.csv*.
3. Por último se genera el diccionario de códigos y se vuelca el resultado en la variable TIPO_COMPROBANTE y en el archivo *output.py*
