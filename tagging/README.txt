PROCESAMIENTO DE LENGUAJE NATURAL 2015 - FaMAF, UNC
====================================================
TRABAJO PRÁCTICO 2
====================================================

AUTOR:
CAPELLO, AGUSTÍN ALDO
capelloagustin@gmail.com
GitHub: acapello

Página del enunciado del proyecto:
http://cs.famaf.unc.edu.ar/wiki/materias/pln/practico2

Nota: Para ejecutar este proyecto (y los demás) es necesario haber instalado
todos los requerimientos descriptos en PLN-2015/README.rst y correr TODOS
los comandos desde la carpeta raíz (PLN-2015/), estando en el virtualenv.
Esto se logra, luego de haber configurado apropiadamente:
$ workon pln-2015
Y el prompt debería quedar parecido a lo siguiente:
(pln-2015):~[some-folders...]/PLN-2015$


ENTRENAR TODOS LOS MODELOS:
Se provee un script para entrenar modelos Baseline, MLHMM y MEMM. n={1,2,3,4}
Es necesario ubicar el corpus en el directorio adecuado, es decir, en
PLN-2015/corpus/ancora-2.0, de lo contrario deben modificarse los scripts
train.py y eval.py en las lineas 42 y 50 respectivamente para cargar el corpus
correctamente.

PLN-2015$ sh tagging/scripts/train_all_models.sh > train_output.txt
Tiempo estimado de ejecución: 50min a 1h 20min

EVALUAR TODOS LOS MODELOS:

PLN-2015$ sh tagging/scripts/eval_all_models.sh > eval_output.txt
Tiempo estimado de ejecución: 2hs a 2hs 30min

Hint: Comentar/descomentar la linea de "progress" de eval.py si se quiere
guardar la salida en un archivo/ver en terminal.


EJERCICIO 1: Corpus Ancora: Estadísticas de etiquetas POS
stats.py: Estadísticas del extraídas de las oraciones etiquetadas del corpus.
Se utiliza la clase Counter() de la librería collections por el uso del método
most_common(n) que devuelve los n mas frecuentes.

Ejecución:
PLN-2015$ python tagging/scripts/stats.py

-----Estadísticas básicas:-------------------------------------------------
    Cantidad de oraciones: 17379
    Cantidad de ocurrencias de palabras: 517268
    Cantidad de palabras (vocabulario): 46482
    Cantidad de etiquetas (vocabulario de tags): 48

-----Etiquetas más frecuentes:---------------------------------------------
    Etiqueta: 'nc'  Frecuencia: 92002  Porcentaje del total: 17.79
    Palabras más frecuentes con la etiqueta 'nc':
        años : 849
        presidente : 682
        millones : 616
        equipo : 457
        partido : 438

    Etiqueta: 'sp'  Frecuencia: 79904  Porcentaje del total: 15.45
    Palabras más frecuentes con la etiqueta 'sp':
        de : 28475
        en : 12114
        a : 8192
        del : 6518
        con : 4150

    Etiqueta: 'da'  Frecuencia: 54552  Porcentaje del total: 10.55
    Palabras más frecuentes con la etiqueta 'da':
        la : 17897
        el : 14524
        los : 7758
        las : 4882
        El : 2817

    Etiqueta: 'vm'  Frecuencia: 50609  Porcentaje del total: 9.78
    Palabras más frecuentes con la etiqueta 'vm':
        está : 564
        tiene : 511
        dijo : 499
        puede : 381
        hace : 350

    Etiqueta: 'aq'  Frecuencia: 33904  Porcentaje del total: 6.55
    Palabras más frecuentes con la etiqueta 'aq':
        pasado : 393
        gran : 275
        mayor : 248
        nuevo : 234
        próximo : 213

    Etiqueta: 'fc'  Frecuencia: 30148  Porcentaje del total: 5.83
    Palabras más frecuentes con la etiqueta 'fc':
        , : 30148

    Etiqueta: 'np'  Frecuencia: 29113  Porcentaje del total: 5.63
    Palabras más frecuentes con la etiqueta 'np':
        Gobierno : 554
        España : 380
        PP : 234
        Barcelona : 232
        Madrid : 196

    Etiqueta: 'fp'  Frecuencia: 21157  Porcentaje del total: 4.09
    Palabras más frecuentes con la etiqueta 'fp':
        . : 17513
        ( : 1823
        ) : 1821

    Etiqueta: 'rg'  Frecuencia: 15333  Porcentaje del total: 2.96
    Palabras más frecuentes con la etiqueta 'rg':
        más : 1707
        hoy : 772
        también : 683
        ayer : 593
        ya : 544

    Etiqueta: 'cc'  Frecuencia: 15023  Porcentaje del total: 2.90
    Palabras más frecuentes con la etiqueta 'cc':
        y : 11211
        pero : 938
        o : 895
        Pero : 323
        e : 310


-----Niveles de ambigüedad de las palabras:------------------------------
    Ambigüedad: 1  Cantidad de palabras: 44109  Porcentaje del total: 94.89
    Palabras más frecuentes con ambigüedad 1:
        , : 30148
        el : 14524
        en : 12114
        con : 4150
        por : 4087

    Ambigüedad: 2  Cantidad de palabras: 2194  Porcentaje del total: 4.72
    Palabras más frecuentes con ambigüedad 2:
        la : 18100
        y : 11212
        " : 9296
        los : 7824
        del : 6519

    Ambigüedad: 3  Cantidad de palabras: 153  Porcentaje del total: 0.33
    Palabras más frecuentes con ambigüedad 3:
        . : 17520
        a : 8200
        un : 5198
        no : 3300
        es : 2315

    Ambigüedad: 4  Cantidad de palabras: 19  Porcentaje del total: 0.04
    Palabras más frecuentes con ambigüedad 4:
        de : 28478
        dos : 917
        este : 830
        tres : 425
        todo : 393

    Ambigüedad: 5  Cantidad de palabras: 4  Porcentaje del total: 0.01
    Palabras más frecuentes con ambigüedad 5:
        que : 15391
        mismo : 247
        cinco : 224
        medio : 105

    Ambigüedad: 6  Cantidad de palabras: 3  Porcentaje del total: 0.01
    Palabras más frecuentes con ambigüedad 6:
        una : 3852
        como : 1736
        uno : 335

    Ambigüedad: 7  Cantidad de palabras: 0  Porcentaje del total: 0.00

    Ambigüedad: 8  Cantidad de palabras: 0  Porcentaje del total: 0.00

    Ambigüedad: 9  Cantidad de palabras: 0  Porcentaje del total: 0.00
-------------------------------------------------------------------------


EJERCICIO 3: Entrenamiento y Evaluación de Taggers

Entrenar un modelo:
PLN-2015$ python tagging/scripts/train.py [-n <n>] [-m <model>] -o <file>
<n> ::= [1 | 2 | 3 | 4]   (no es utilizado en baseline)
<model> ::= [base | mlhmm | memm]

Evaluar un modelo:
PLN-2015$ python tagging/scripts/eval.py -i <file>

Para calular la matriz de confusión se hace uso de la función que provee la
librería de scikit learn. También se hace uso de matplotlib.pyplot para
graficarla, y se la guarda en formatos .txt y .png (usar zoom).


EJERCICIO 2: Baseline Tagger
Un etiquetador básico, que etiqueta cada palabra con su tag más frecuente.
Tests:
nosetests tagging/tests/test_baseline.py

RESULTADOS:

Accuracy (global):                      89.04%
Accuracy sobre palabras conocidas:      95.36%
Accuracy sobre palabras desconocidas:   31.80%

Tiempo (en segundos)
real 11.92sec
user 11.40
sys   0.20

Matriz de confusión en base-confusion-matrix.png, .txt

Entrenar y evaluar el modelo:
PLN-2015$ python tagging/scripts/train.py -m base -o base
PLN-2015$ python tagging/scripts/eval.py -i base
Se deberán imprimir los resultados de accuracy mostrados arriba, y la matriz de
confusión (se recomienda consola full screen)
(análogo para los siguientes modelos)


EJERCICIO 4: Hidden Markov Models y Algoritmo de Viterbi
Tests:
nosetests tagging/tests/test_hmm.py
nosetests tagging/tests/test_viterbi_tagger.py


EJERCICIO 5: HMM POS Tagger
Tests:
nosetests tagging/tests/test_ml_hmm.py

RESULTADOS:
n = 1
Accuracy (global):                      89.01%
Accuracy sobre palabras conocidas:      95.32%
Accuracy sobre palabras desconocidas:   31.80%

real 36.94sec
user 36.31
sys   0.29

n = 2
Accuracy (global):                      92.72%
Accuracy sobre palabras conocidas:      97.61%
Accuracy sobre palabras desconocidas:   48.42%

real 68.54sec
user 67.99
sys   0.24

n = 3
Accuracy (global):                      93.17%
Accuracy sobre palabras conocidas:      97.67%
Accuracy sobre palabras desconocidas:   52.31%

real 256.31sec
user 255.71
sys   0.33

n = 4
Accuracy (global):                      93.14%
Accuracy sobre palabras conocidas:      97.44%
Accuracy sobre palabras desconocidas:   54.14%

real 1484.23sec
user 1483.50
sys   0.82


EJERCICIO 6: Features para Etiquetado de Secuencias
Tests:
nosetests tagging/tests/test_features.py


EJERCICIO 7: Maximum Entropy Markov Models
Tests:
nosetests tagging/tests/test_memm.py

RESULTADOS:
Clasificador LogisticRegression
n = 1
Accuracy (global):                      92.70%
Accuracy sobre palabras conocidas:      95.28%
Accuracy sobre palabras desconocidas:   69.32%

real 75.12sec
user 73.89
sys   0.30

n = 2
Accuracy (global):                      92.70%
Accuracy sobre palabras conocidas:      95.28%
Accuracy sobre palabras desconocidas:   69.32%

real 75.27sec
user 74.21
sys   0.22

n = 3
Accuracy (global):                      91.99%
Accuracy sobre palabras conocidas:      94.55%
Accuracy sobre palabras desconocidas:   68.75%

real 80.60sec
user 79.54
sys   0.24

n = 4
Accuracy (global):                      92.18%
Accuracy sobre palabras conocidas:      94.72%
Accuracy sobre palabras desconocidas:   69.20%

real 86.14sec
user 84.94
sys   0.26

Clasificador MultinomialNB
n = 1
Accuracy (global):                      82.18%
Accuracy sobre palabras conocidas:      85.85%
Accuracy sobre palabras desconocidas:   48.89%

real 1439.07sec
user 1437.63
sys   0.28

n = 2
Accuracy (global):                      82.18%
Accuracy sobre palabras conocidas:      85.85%
Accuracy sobre palabras desconocidas:   48.89%

real 1439.43sec
user 1437.82
sys   0.30

n = 3
Accuracy (global):                      76.46%
Accuracy sobre palabras conocidas:      80.41%
Accuracy sobre palabras desconocidas:   40.68%

real 1226.13sec
user 1225.88
sys   0.42

n = 4
Accuracy (global):                      71.47%
Accuracy sobre palabras conocidas:      75.09%
Accuracy sobre palabras desconocidas:   38.59%

real 1154.15sec
user 1153.83
sys   0.55


Clasificador LinearSVC
n = 1
Accuracy (global):                      94.43%
Accuracy sobre palabras conocidas:      97.04%
Accuracy sobre palabras desconocidas:   70.82%

real 68.21sec
user 67.82
sys   0.12

n = 2
Accuracy (global):                      94.43%
Accuracy sobre palabras conocidas:      97.04%
Accuracy sobre palabras desconocidas:   70.82%

real 73.25sec
user 72.72
sys   0.24

n = 3
Accuracy (global):                      94.29%
Accuracy sobre palabras conocidas:      96.91%
Accuracy sobre palabras desconocidas:   70.57%

real 81.06sec
user 80.52
sys   0.25

n = 4
Accuracy (global):                      94.40%
Accuracy sobre palabras conocidas:      96.94%
Accuracy sobre palabras desconocidas:   71.38%

real 85.23sec
user 84.73
sys   0.22
