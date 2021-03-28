**Diccionario tipos de comprobante AFIP**

Este es un diccionario en formato Python con los códigos de tipo de comprobante de AFIP y su descripción.
Para los interesados pueden obtener directamente el diccionario con el formato
```
{1:'FACTURAS A',2:'NOTAS DE DEBITO A',3:'NOTAS DE CREDITO A'....}
```
en el archivo *output.py*

Para aquellos interesados en reutilizar el código en el caso de futuros cambios en AFIP:

El archivo en formato Excel *TABLACOMPROBANTES.xls* lo descargué del sitio de AFIP:
[AFIP] (http://www.afip.gov.ar/fe/documentos/tablas%20generales%20v.0.1%20%2026012011.xls)
y luego lo exporté como archivo de texto (comma separated values) *TABLACOMPROBANTES.csv*

Corriendo el script *main.py* se genera el diccionario de códigos y se vuelca el resultado en la variable TIPO_COMPROBANTE y en el archivo *output.py*
