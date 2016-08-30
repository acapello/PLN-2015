PROCESAMIENTO DE LENGUAJE NATURAL 2015 - FaMAF, UNC
====================================================
TRABAJO PRÁCTICO 4
====================================================
TEMA:
4. Segmentación de Usuarios de Twitter

Propuesto por: Laura

Segmentación (clustering) de usuarios de twitter a partir del texto de sus tweets, y luego visualización de los contenidos de los segmentos usando metadatos demográficos (nombre, ubicación geográfica, edad, sexo) y alguna forma de wordcloud.

Referencia principal:

http://www.ee.columbia.edu/~lyndon/pubs/wsm2009-twitter.pdf
====================================================

AUTOR:
CAPELLO, AGUSTÍN ALDO
capelloagustin@gmail.com
GitHub: acapello

Nota: Para ejecutar este proyecto (y los demás) es necesario haber instalado
todos los requerimientos descriptos en PLN-2015/README.rst y correr TODOS
los comandos desde la carpeta raíz (PLN-2015/), estando en el virtualenv.
Esto se logra, luego de haber configurado apropiadamente:
$ workon pln-2015
Y el prompt debería quedar parecido a lo siguiente:
(pln-2015):~[some-folders...]/PLN-2015$

EJEMPLOS PARA ENTRENAR/EVALUAR:

Entrenar un modelo:
PLN-2015$ python clustering/scripts/train.py -o model
Nota: predeterminadamente, se entrena el modelo buscando 8 clusters con el algoritmo K-Means.


Evaluar un modelo:
PLN-2015$ python clustering/scripts/eval.py -i model
Nota: es recomendado redirigir la salida a un archivo.
Las nubes de palabras de cada cluster se encontrarán en la carpeta clustering/wordclouds.


Obtener información del usuario con id 117866979 (como sus tweets y nombre):
PLN-2015$ python clustering/scripts/print_user_data.py -u 117866979 -i model


Obtener información de los 10 usuarios más relevantes del cluster 5:
PLN-2015$ python clustering/scripts/print_relevant_users.py -i model -c 5 -n 10



MODULOS REQUERIDOS:
featureforge
sklearn
pickle
wordcloud
matplotlib