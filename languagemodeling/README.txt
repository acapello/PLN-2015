PROCESAMIENTO DE LENGUAJE NATURAL 2015 - FaMAF, UNC
====================================================
TRABAJO PRÁCTICO 1
====================================================


AUTOR:
CAPELLO, AGUSTÍN ALDO
capelloagustin@gmail.com
GitHub: acapello

Página del enunciado del proyecto:
http://cs.famaf.unc.edu.ar/wiki/materias/pln/practico1

Nota: Para ejecutar este proyecto (y los demás) es necesario haber instalado
todos los requerimientos descriptos en PLN-2015/README.rst y correr TODOS
los comandos desde la carpeta raíz (PLN-2015/), estando en el virtualenv.
Esto se logra, luego de haber configurado apropiadamente:
$ workon pln-2015
Y el prompt debería quedar parecido a lo siguiente:
(pln-2015):~[some-folders...]/PLN-2015$

EJERCICIO 1: Corpus

Se obtuvo de la Web una serie de libros en en español, en formato .txt.
Todos están uno luego del otro en el archivo training.txt (7.1 MB)
Entre ellos se encuentran obras de Arthur Conan Doyle, C. S. Lewis, Julio Verne,
y otros autores.



EJERCICIO 2: Modelo de n-gramas
Se agregó el método perplexity. Todos los modelos (AddOne, Interpolated, Backoff)
heredan de la clase NGram

Ejecutar los tests del módulo NGram:
nosetests languagemodeling/tests/test_ngram.py



EJERCICIO 3: Generación de Texto
Ejemplos de oraciones generadas con modelos NGram, utilizando el script generate.py:

Unigramas

Durante hoguera Bartholomew aquellos dientes súbita sin 5 pie ponga admire Clark

John repuso son , hay lo es ni metí quitar había terrible de ! dar Podía que Debbie enviado , un En en me estériles había Una muro un usted noche . pregunté lanzaré . sangre para Vancha , Pensaba obtendrás y agobiante - quedarme sillas . inconsciente - prefiere Deja muchas alarma y una — En me las navegó parte era

gélidas la espíritu de el levanta casi

Nunca una a barrera . a las bar círculo de o


Bigramas

Tiny y principios se puso una ignota eternidad al levantarme al hundirse en el amigo de estar sola palabra -.

De sus presas más que vi la irritación de que matarían !

—¡ Cuidado , Alemania , mirando al final del Padre , ¡ Dame las brujas .

Claro que nunca lo bastante para la copa anual de la Catedrática y Sociología , cojeando alrededor parecía mirarle como los primeros rastros de raro : - Me quedé donde Biao y reunirte con ella , pero ambos un empujón relativamente cerca de balonmano ... Me llamo Darren .


Trigramas

En el ciclo creativo , el conductor todavía no la dejamos levantarse hasta la que habíamos hecho durante los doce años siendo compañeros y abandonó el escenario del Estudio C nadie se metería conmigo mientras fuera la muerte de Rosalie .

-¿ Van a arrestar a Jason ?

Veo que tienes que contarme algo sobre que contenía diecisiete piedras , los volúmenes .

Antes había estado observando angustiada a Jonathan .

Después de instalarme , descendí al estudio de mucho interés .


Cuatrigramas

Aterricé con suavidad , y cerró la puerta y entramos en el laboratorio de química del hospital .

Al final de ella hay una boya con una campana , que suena cuando hay mal tiempo y lanza sus lúgubres notas al viento .

El señor Abel White era un hombre bueno e inteligente .

Nunca pensé que pudieras llegar a olvidarte .

Cuando regresé de entre los físicos , Demócrito se limitó a toser tras su puño .

¡ Fue tan agradable poder sentir tu simpatía !



TESTS: nosetests languagemodeling/tests/test_ngram_generator.py



EJERCICIO 4: Suavizado "add-one"
Resultados de Perplexity debajo

TESTS: nosetests languagemodeling/tests/test_addone_ngram.py



EJERCICIO 5: Evaluación de Modelos de Lenguaje
Resultados de Perplexity debajo. Programado el script eval.py, y para
ello la clase Eval, en NGram, la cual calcula de manera más eficiente los tres
parámetros de interés.



EJERCICIO 6: Suavizado por Interpolación
Resultados de Perplexity debajo


TESTS: nosetests languagemodeling/tests/test_interpolated_ngram.py



EJERCICIO 7: Suavizado por Back-Off con Discounting
Resultados de Perplexity debajo



TESTS: nosetests languagemodeling/tests/test_backoff_ngram.py




RESULTADOS DE PERPLEXITY
Utilizando el script eval.py

Orden           |        1         |       2         |        3         |     4

NGram           |        inf       |      inf        |       inf        |     inf

Add-One         |   1303.291309    |   3612.759288   |   27939.970358   |  50073.855

Interpolated    |   1301.364075    |   319.840250    |   380.100998     |  605.988625
                    (Gamma:1.0)        (Gamma:250.0)    (Gamma:250.0)     (Gamma:75.0)

BackOff         |   1301.364075    |   261.497105    |   230.284771     |  227.868515
                    (Beta:0.1)        (Beta:0.7)        (Beta:0.8)         (Beta:0.8)




ENTRENAR TODOS LOS MODELOS:
Se provee un script para entrenar todos los modelos, hasta cuatrigramas.


PLN-2015$ sh languagemodeling/scripts/train_all_models.sh


Aproximadamente el tiempo de ejecución del script es de 10 minutos con un procesador
Intel i5- i7
En output se podrán apreciar impresiones del programa, como por ejemplo
la sucesiva selección de gammas y betas.


EVALUAR TODOS LOS MODELOS:

PLN-2015$ sh languagemodeling/scripts/eval_all_models.sh

Tiempo de demora aproximado: 2 minutos
