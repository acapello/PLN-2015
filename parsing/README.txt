PROCESAMIENTO DE LENGUAJE NATURAL 2015 - FaMAF, UNC
====================================================
TRABAJO PRÁCTICO 3
====================================================

AUTOR:
CAPELLO, AGUSTÍN ALDO
capelloagustin@gmail.com
GitHub: acapello

Página del enunciado del proyecto:
http://cs.famaf.unc.edu.ar/wiki/materias/pln/practico3

Nota: Para ejecutar este proyecto (y los demás) es necesario haber instalado
todos los requerimientos descriptos en PLN-2015/README.rst y correr TODOS
los comandos desde la carpeta raíz (PLN-2015/), estando en el virtualenv.
Esto se logra, luego de haber configurado apropiadamente:
$ workon pln-2015
Y el prompt debería quedar parecido a lo siguiente:
(pln-2015):~[some-folders...]/PLN-2015$


ENTRENAR TODOS LOS MODELOS:
Se provee un script para entrenar modelos Baseline, UPCFG.
Es necesario ubicar el corpus en el directorio adecuado, es decir, en
PLN-2015/corpus/ancora-2.0, de lo contrario deben modificarse los scripts
train.py y eval.py para cargar el corpus correctamente.

PLN-2015$ sh train_all_models.sh

EVALUAR TODOS LOS MODELOS:
PLN-2015$ sh eval_all_models.sh

Hint: Comentar/descomentar la linea de "progress" de eval.py si se quiere
guardar la salida en un archivo/ver en terminal el progreso.

Entrenar y evaluar todo:
PLN-2015$ sh train_all_models.sh && sh eval_all_models.sh

Por defecto el standard output se guarda en archivos models/train_output.txt,
models/eval_output.txt junto a los modelos entrenados


EJERCICIO 1: Evaluación de Parsers
------------------------------------------------
Archivos: scripts/eval.py scripts/train.py

Entrenar un modelo:
PLN-2015$ python parsing/scripts/train.py [-n <n>] [-m <model>] -o <file>
<n> ::= [0 | 1 | 2 | 3 | ...]   (orden de markovización horizontal para upcfg)
<model> ::= [flat | rbranch | lbranch | upcfg]

Evaluar un modelo:
tagging/scripts$ python parsing/scripts/eval.py -i <file>


Resultados de los modelos “baseline” para oraciones de largo menor o igual a 20
-------------------------------------------------------------------------------
Archivo: baselines.py

- Flat:

Model type: <class 'parsing.baselines.Flat'>

* Parsed 1444 sentences
* Labeled
  - Precision: 99.93%
  - Recall: 14.57%
  - F1: 25.43%
* Unlabeled
  - Precision: 100.00%
  - Recall: 14.58%
  - F1: 25.45%

real 7.87
user 7.78
sys 0.09
(tiempo en segundos)

- RBranch:

Model type: <class 'parsing.baselines.RBranch'>

* Parsed 1444 sentences
* Labeled
  - Precision: 8.81%
  - Recall: 14.57%
  - F1: 10.98%
* Unlabeled
  - Precision: 8.87%
  - Recall: 14.68%
  - F1: 11.06%

real 8.56
user 8.46
sys 0.09

- LBranch:

Model type: <class 'parsing.baselines.LBranch'>

* Parsed 1444 sentences
* Labeled
  - Precision: 8.81%
  - Recall: 14.57%
  - F1: 10.98%
* Unlabeled
  - Precision: 14.71%
  - Recall: 24.33%
  - F1: 18.33%

real 8.71
user 8.63
sys 0.07


EJERCICIO 2: Algoritmo CKY
-----------------------------
Archivo: cky_parser.py

Se implementó el algoritmo CKY que, dada una UPCFG binarizada, encuentra el
"mejor" árbol sintáctico (el más adecuado dado el modelo) junto a su
log-probabilidad.


EJERCICIO 3: PCFGs No Lexicalizadas
-------------------------------------
Archivo: upcfg.py


Resultados de UPCFG para oraciones de largo menor o igual a 20
----------------------------------------------------------------


n = None (sin Markovización Horizontal)
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  - Precision: 73.22%
  - Recall: 72.92%
  - F1: 73.07%
* Unlabeled
  - Precision: 75.33%
  - Recall: 75.02%
  - F1: 75.18%

real 311.28
user 310.24
sys 0.95


EJERCICIO 4: Markovización Horizontal
--------------------------------------
Archivo: upcfg.py


Resultados de UPCFG para oraciones de largo menor o igual a 20
----------------------------------------------------------------

n = 0
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  - Precision: 70.25%
  - Recall: 70.02%
  - F1: 70.14%
* Unlabeled
  - Precision: 72.11%
  - Recall: 71.88%
  - F1: 72.00%

real 104.10
user 104.00
sys 0.08


n = 1
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  - Precision: 74.66%
  - Recall: 74.57%
  - F1: 74.61%
* Unlabeled
  - Precision: 76.53%
  - Recall: 76.43%
  - F1: 76.48%

real 130.44
user 130.27
sys 0.13


n = 2
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  - Precision: 74.80%
  - Recall: 74.28%
  - F1: 74.54%
* Unlabeled
  - Precision: 76.72%
  - Recall: 76.19%
  - F1: 76.45%

real 223.45
user 223.11
sys 0.32


n = 3
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  - Precision: 74.03%
  - Recall: 73.39%
  - F1: 73.71%
* Unlabeled
  - Precision: 76.19%
  - Recall: 75.54%
  - F1: 75.86%

real 280.07
user 279.52
sys 0.52
