PROCESAMIENTO DE LENGUAJE NATURAL 2015 - FaMAF, UNC
====================================================
PRÁCTICO 3
====================================================


AUTOR:
CAPELLO, AGUSTÍN ALDO
capelloagustin@gmail.com
GitHub: acapello

Página del enunciado del proyecto:
http://cs.famaf.unc.edu.ar/wiki/materias/pln/practico3


ENTRENAR TODOS LOS MODELOS:
Se provee un script para entrenar modelos Baseline, UPCFG.
Es necesario ubicar el corpus en el directorio adecuado, es decir, en
PLN-2015/corpus/ancora-2.0, de lo contrario deben modificarse los scripts
train.py y eval.py para cargar el corpus correctamente.

parsing/scripts$ sh train_all_models.sh

EVALUAR TODOS LOS MODELOS:
parsing/scripts$ sh eval_all_models.sh

Hint: Comentar/descomentar la linea de "progress" de eval.py si se quiere
guardar la salida en un archivo/ver en terminal el progreso.

Entrenar y evaluar todo:
parsing/scripts$ sh train_all_models.sh && sh eval_all_models.sh

Por defecto el standard output se guarda en archivos models/train_output.txt,
models/eval_output.txt junto a los modelos entrenados


EJERCICIO 1: Evaluación de Parsers
------------------------------------------------
Archivos: scripts/eval.py scripts/train.py

Entrenar un modelo:
parsing/scripts$ python3.4 train.py [-n <n>] [-m <model>] -o <file>
<n> ::= [0 | 1 | 2 | 3 | ...]   (orden de markovización horizontal para upcfg)
<model> ::= [flat | rbranch | lbranch | upcfg]

Evaluar un modelo:
tagging/scripts$ python3.4 eval.py -i <file>


Resultados de los modelos “baseline” para oraciones de largo menor o igual a 20
-------------------------------------------------------------------------------
Archivo: baseline.py

- Flat:

Model type: <class 'parsing.baselines.Flat'>

* Parsed 1444 sentences
* Labeled
  * Precision: 99.93%
  * Recall: 14.57%
  * F1: 25.43%
* Unlabeled
  * Precision: 100.00%
  * Recall: 14.58%
  * F1: 25.45%

real 8.85
user 7.65
sys 0.21
(tiempo en segundos)

- RBranch:

Model type: <class 'parsing.baselines.RBranch'>

* Parsed 1444 sentences
* Labeled
  * Precision: 8.81%
  * Recall: 14.57%
  * F1: 10.98%
* Unlabeled
  * Precision: 8.87%
  * Recall: 14.68%
  * F1: 11.06%

real 13.75
user 13.63
sys 0.12

- LBranch:

Model type: <class 'parsing.baselines.LBranch'>

* Parsed 1444 sentences
* Labeled
  * Precision: 8.81%
  * Recall: 14.57%
  * F1: 10.98%
* Unlabeled
  * Precision: 14.71%
  * Recall: 24.33%
  * F1: 18.33%

real 18.59
user 18.39
sys 0.18


EJERCICIO 2: Algoritmo CKY
-----------------------------
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
  * Precision: 73.05%
  * Recall: 72.75%
  * F1: 72.90%
* Unlabeled
  * Precision: 75.16%
  * Recall: 74.85%
  * F1: 75.00%

real 326.37
user 322.82
sys 3.51


EJERCICIO 4: Markovización Horizontal
--------------------------------------
Archivo: upcfg.py


Resultados de UPCFG para oraciones de largo menor o igual a 20
----------------------------------------------------------------

n = 0
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  * Precision: 70.18%
  * Recall: 69.95%
  * F1: 70.06%
* Unlabeled
  * Precision: 72.04%
  * Recall: 71.81%
  * F1: 71.93%

real 197.78
user 197.69
sys 0.11


n = 1
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  * Precision: 74.71%
  * Recall: 74.62%
  * F1: 74.66%
* Unlabeled
  * Precision: 76.58%
  * Recall: 76.48%
  * F1: 76.53%

real 186.05
user 185.85
sys 0.21


n = 2
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  * Precision: 74.81%
  * Recall: 74.29%
  * F1: 74.55%
* Unlabeled
  * Precision: 76.73%
  * Recall: 76.20%
  * F1: 76.46%

real 219.71
user 219.42
sys 0.38


n = 3
Model type: <class 'parsing.upcfg.UPCFG'>

* Parsed 1444 sentences
* Labeled
  * Precision: 73.92%
  * Recall: 73.28%
  * F1: 73.60%
* Unlabeled
  * Precision: 76.08%
  * Recall: 75.42%
  * F1: 75.75%

real 277.70
user 277.08
sys 0.72
