# Python Advanced
## Loops (bucles)
Un bucle es una estructura de control que permite ejecutar un bloque de codigo repetidamente mientrs se cumpla una condicion o mientras existan elementos en un coleccion.

Se usan para automatizar tareas repetitivas,  evitardo  tener que escribir el mismo codigo muchas veces.

Los bucles permiten recorrer colecciones de datos, repetir calculos, procesar informacion elemento a elemento y ejecutar codigo hasta que ocurra una condicion especifica.

Ha dos tipos de bucles_

- while
- for ... in

### While
Ejecuta un bloque de codigo mientra una condicion logica sea verdadera.
El programa evalua la condicion antes de cada iteracion y si la condicion es verdadera, el codigo se ejecuta, si es falsa el bucle termina.
While no tiene fin definido no se parara si no se este iterando, hay que decirle cuando pararse. Hay que configurar un valor centinela 

#### Funcionamiento conceptual
```
comprobar condición
      │
      ▼
¿condición verdadera?
      │
   sí ─────► ejecutar código
      │
      ▼
volver a comprobar condición
```

En un bucle while es necesario actualizar la condicion dentro del bucle, de lo contrario se puede crear un bucle infinito.

### For ... in

Se utiliza para recorrer  los elementos de una coleccion o iterable ejecutando un bloque de codigo para cada elemento.

For .. in permite itera sobre cada elemento de una sestructura de datos, un iterable es cualquier objeto que pueda recorrerse elemento por elemento como listas, tuplas sets, diccionarios, strings, rangos.
Con for tienes un principio y un fin bien definidos

#### Funcionamiento conceptual
```
colección de datos

[elemento1, elemento2, elemento3]

for elemento in colección:

    ejecutar código
```
### For ... range()

range() es un funcion integrada en phython que genera un una secuencia de numero enteros que se utiliza para controlas cuantas veces se ejecutara un bucle. No crea una lista real de numeros sino un lista iterable que produce numeros cuando el bucle los necesita.

#### range(stop)
Cuando le damos un solo numero es el de stop

```

range(5)
↓
0,1,2,3,4

el ultimo lo excluye
```
#### range(start, stop)

Cuando le damos dos numeros el primero es por el que empieza y acaba antes del ultimo

```

range(1,10)
↓
1,2,3,4,5,6,7,8,9

el ultimo lo excluye
```
#### range(start, stop, step)
Cuando le damos tres numeros empieza por el primero acaba por el segundo y avanza por el tercero
El tercero le indica de cuanto en cuanto avanza los numeros
```

for num in range(1,10,2):
   print(num)

empezar en 1
terminar antes de 10
avanzar de 2 en 2
```

#### Break
Break es la palabra clave que permite interrumpir inmediatamente un bucle, el proposito es salir del bucle cuando se 
cumple la condicion especifica, un uso tipico es detener el bucle  al encontrar un valor buscado o evitar procesamiento adicional
cuando ya se alcanzo el objetivo.
Break detiene el bucle por completo incluso si todavia quedan elementos por iterar. 
```python
lenguajes =['Go', 'Java', 'Ruby', 'Python', 'Swift', 'PHP']
for lenguaje in lenguajes:
    if lenguaje == "Python":
        print(f"{lenguaje} fue encontrado en la posición {lenguajes.index(lenguaje)}")
        break
    print(lenguaje)
    
```
#### Continue
Continue  es una palabra clave que permite saltar la iteracion actual de un bucle y continuar con la siguiente iteracion. 
Omite ciertas iteraciones que cumplen una condicion, sin deterner el bucle completo. Se usa para saltar elementos no deseados e ignorar
casos especificos mientras se sigue procesando el resto de la secuencia.
Continue no termina el bucle, solo omite la iteracion actual.
```python
lenguajes =['Java', 'Ruby', 'Python', 'Swift', 'PHP']

for lenguaje in lenguajes:
    if lenguaje == "Python":
        print(f"No procesamos {lenguaje}, seguimos con los demás...")
        continue
    print(f"{lenguaje} será procesado normalmente")

```
## Lista compresiva

Una list Comprehension es una estructura que permite crear un lista nueva aplicando una expresion a cada elemento de una secuencia.

#### Forma General
[expresion for elemento in iterable]

- expresion: lo que quieres hacer con cada elemento

- elemento: variable temporal

- iterable: lista, string, etc

```
words = ["python","java","rust"]

result = [word.upper() for word in words]

print(result)
```

#### Con condicionales (if)

Permite filtrar  y modificar elementos de una secuenccia  en una sola linea sustituyendo la combinacion de un bucle for y una condicion if tradicional.
[expresion for elemento in iterable if condicion]

La expresion es la transformacion que se aplica al elemento, El elememento es la variable que representa cada valor iterable, el iterable es la coleccion que se recorre y la condicion es el criterio que determina si el elemento se incluye en la nueva lista.


```
numbers = [1,2,3,4,5,6]

result = [number * 2 for number in numbers if number % 2 == 0]

print(result)
```


No se recomienda usarla si la logica es muy compleja ya no se veria claro que es lo tiene que hacer



## Condicionales If
El condicional if es una estructura de control de flujo que permite tomar decisiones dentro de un programa, ejecutando un bloque de codigo solo cuando la condicion logica se cumple(es decir cuando es True)

Lo que es lo mismo if permite que el programa evalue una expresion booleana y dependiendo del resultado, ejecuta o ignora ciertas intruccciones.

Un programa normalmente se ejecuta de arriba hacia abajo pero con if podemos cambiar el flujo.

Primero se evalua la condicion, si el resultado en True se ejecuta el  bloque de codigo asociado, si es False  se omite ese bloque

#### Uso del else

else permite ejecutar codigo cuando la condicioin if es false

#### Uso del elif
elif (else if) permite evaluar multiple condiciones

El condicional if es una estructura fundamental en python que permite controlar el flujo del programa evaluando condiciones logicca, ejecutando diferentes bloques de codigo segun si dichas condiciones son verdaderas o falsas.
Se utiliza para tomar decisiones, validar datos, controlar procesos y dirigir la logica del programa, siendo una de las herramientas mas importantes de la progrmacion.

## Operador Ternario
Es la forma abreviada de escribir una estructura condicional if-else en una sola linea. Permite evaluar una condicion y devolver un valor u otro dependiendo de si la condicion es verdadera o falsa.
Se llama ternario porque esta formado por tres partes:
      - El valor que se devuelve si la condicion es verdadera
      - La conddicion que se evalua
      - El valor que se devuelve si la condicion es falsa.

Su objetivo principal es simplificar expresiones condicionales simples, haciendo el codigo mas compacto y legible cuando solo se necesita elegir entre dos resultados.
```
valor_si_true if condicion else valor_si_false
```
## Operador ternario en expresiones
Puede usarse dentro de expresiones lo que significa que puede formar parte de una asignacion, una operacion o una funcion.En este caso el operador evalua la condicion y devuelve uno de dos valores posibles dependiendo del resultado.

```
resultado = "aprobado" if nota >= 5 else "suspenso"
```
En este cado evalua la condicion "nota >=5" si es verdadera, la variable resultado toma el valor "aprobado"
si es falsa toma el valor "suspenso"

Esto permite integrar decisiones dentro de calculos o asignaciones, haciendo el codigo mas compacto cuando lo existe dos posibles resultados
## Operador Ternario en Listas

Los operadores ternaarios tambien pueden usar en listas compresivas para transformar los elementos de una coleccion segun una condicion.
En este contexto, el operador ternario permite qu ecada elemento de la lista resultante dependa de una evaluacion lógica aplicada a cada elemento del iterable.
```
[valor_si_true if condicion else valor_si_false for elemento in iterable]
```

El operador ternario permite introducir lógica condicional dentro de una expresión, devolviendo uno de dos valores según el resultado de una condición.
Cuando se usa dentro de listas comprensivas, permite generar nuevas listas cuyos elementos dependen de una evaluación condicional aplicada a cada elemento del iterable.


## Operadores de comparacion

```
| Operador |       Significado      |  Ejemplo |        Resultado             |
|----------|------------------------|----------|------------------------------|
| ==       | Igual a                | `x == y` | True si son iguales          |
| !=       | Distinto de            | `x != y` | True si son diferentes       |
| <>       | Distinto de (obsoleto) | `x <> y` | Igual que `!=`, ya no se usa |
| >        | Mayor que              | `x > y`  | True si x es mayor           |
| <        | Menor que              | `x < y`  | True si x es menor           |
| >=       | Mayor o igual          | `x >= y` | True si x ≥ y                |
| <=       | Menor o igual          | `x <= y` | True si x ≤ y                |

```


## Operador IN
El operador in es un operador de pertenencia, que se utiliza para comprobar si un elemento se encuentra dentro de una coleccion o una estructtura de datos.
Cuando se utiiza en una condicion if el operacion in evalua si un valor existe dentro de un iterable y devuevlve un valor booleano. True si esta presente, False si no lo esta.

Esto permite tomar decisiones dentro del programa basadas en la presencia o no ausencia de un elemento en una coleccion de datos.

```
elemento in iterable
```
El elemento es el valor que queremos comprobar y el iterable la estructura que contiene los elementos(lista, string, etc). Se recorre el iterable y verifica si el elemento coincide con alguno de los valores almacenados.

## Operador inverso not in
Es la forma contraria a in. Sirve para comprobar que un elemento no esta en una coleccion. Funciona exactamente igual que in pero al contrario. en este caso no contiene el valor que se esta buscando.


## Operadores Logicos
Los operadores logicos se utilizan para combinar, modificar o evalur multiples condiciones dentro de una expresion logica. Son fundamentales para construir condiconales compuestos, es decir, condicionales que dependen de más de un criterio.

Estos operadores trabajan con valores booleanos (True o false) y permiten controlar el flujo de un programa cuando es necesario evaluar varias condiciones al mismo tiempo.

Los tres operadores logicos principales son:
- and 
- or
- not

####  Operador lógico `and`
El operador and se utiliza para combinar dos o mas condicionales y el resultado sera True unicamente si todas las condiciones evaluadas son verdaderas.

```

| Condición A | Condición B | Resultado |
|-------------|-------------|-----------|
| True        | True        | True      |
| True        | False       | False     |
| False       | True        | False     |
| False       | False       | False     |
```
####  Operador lógico `or`
El operador  or se utiliza cuando se quiere al menos una condicon se verdadera para que la expresin  completa sea verdadera.
Solo devuelve false cuando todas las condiciones son falsas.
```

| Condición A | Condición B | Resultado |
|-------------|-------------|-----------|
| True        | True        |      True |
| True        | False       |      True |
| False       | True        |      True |
| False       | False       |     False |

```
#### Operador lógico `not`

El operador not se utiliza para invertir el valor logico de una condicion.

Si La condicion es True, `not` la convierte en False
Si la condicion es False, `not` la convierte en True

```

| Condición | Resultado |
|-----------|-----------|
| True      | False     |
| False     | True      |
```
Prioridad de operadores logicos
```
| Prioridad | Operador |                 Descripción                       |
|-----------|----------|---------------------------------------------------|
| 1         | not      | Niega o invierte el valor lógico                  |
| 2         | and      | True solo si todas las condiciones son verdaderas |
| 3         | or       | True si al menos una condición es verdadera       |

```

## Condicionales Compuestos
Un condicional compuesto es una estructura en la que varias condiciones se combinan mediante operadores logicos (and, or, not) para formar una unica expresion logica.ç
Esto permite construir decisiones mas complejas dentro de un programa, evaluando multiples criterios antes de ejecutar un bloque de codigo.

Gracias a estos operadores es posible construir expresiones lógicas complejas, mejorar el control del flujo del programa y tomar decisiones basadas en múltiples criterios.

## Extended iterable unpacking (operador *)
Es una caracteristica de python que permite descomponer una secuencia en multiples variables, utilizando el operador * para capturar un numero variable de elemento dentro de una lista.

Este mecanimos permite trabajar de forma flexible con estructuras de datos cuando no conocemos exactamente cuantos elementos habra  en una parte determinada de la secuencia.
```
a, b, c = [1,2,3]   # Ejemplo lista
a, b, c = [1,2,3,4] # Da error
a, *b = [1,2,3,4]   # El operador soluciona el error
```

```
first, *rest = [1,2,3,4,5]

first = 1
rest = [2,3,4,5]
```


## Funciones

Las funciones son bloques de codigo reutilizable y organizado que realiza una tarea especifica.
Se define usando la palabra clave def, permitiendo agurpar instruccciones multiples veces, mejorando la modulariddad y evitando repetir codigo. Puede recibir paramentros y devolver resultados usando return.

Reciben como parametros datos de entrada llamados argumentos, que se indica por el usuario o por defecto, los procesan y los devuelven datos de salida.

Las funciones sirven para :

- Dividir y ordenar  el codigo en partes mas sencillas  para depurar y programar con mayor facilidad.
- Reutilizar el codigo, evitando repeticiones  innecesarias.

```
def nombre_funcion(parametros):
    bloque_de_codigo
    return resultado
```

Diferencias entre imprimir y devolver en una funcion es que print muestra informacion al usuario mientras que return envia un valor de vuelta al programa para que pueda ser utilizado posteriormente.

- Imprimir es una accion para visualizar datos en la consola. El valor impreso no se guarda ni puede ser reutilizado por el resto del programa.
- Devolver es una instruccion que finaliza la funcion y "entrega"  un resultado. Este valor puede almacenarse en una variable, pasarse a otra funcion o utilizarse en calculos.


```
| Característica  |	        Imprimir (print)	         | Devolver (return)                            |
|-----------------|--------------------------------------|----------------------------------------------|
| Objetivo	      | Mostrar información.       |	Enviar datos al programa (reutilización).   |
| Destino         | Consola/Pantalla.                    |  El lugar donde se llamó la función.         |
| Almacenamiento  | No se puede guardar en una variable. |	Se puede guardar en una variable.           | 
| Uso Posterior	  | No reutilizable automáticamente.     |  Reutilizable para cálculos.                 |
| Finalización	  | La función continúa.	             |  Finaliza la función inmediatamente.         |
```

## Funciones anidadas en python
Las funciones anidadas tambien llamadas nested functions son un concepto fundamental dentro del diseño de funciones y del manejo del ambito de las variables(scope).
Son funciones dentro de otra funcion lo que permite encapsular logica y acceder a las variables del ambito superior.
De esta forma puedes simplificar el codigo y reutilizar funciones que ya hayas desarrollado en las nuevas funciones que desarrollas.
La funcion exterior se denomina normalmento funcion contenedora, mientras que la funcion definida dentro de ella se conoce como funcion interna.
La funciones anidades resonde a un principo de encapsulacion dentro de la programacion. Esto significa que permite agrupar logica auxiliar dentro de una funcion principal sin exponerla al resto del programa.
La funcion externa defina un entorno local de ejecucion, dentro de ese entorno se pueden declarar subfunciones que pertenecen unicamente a ese contexto.
Por lo tanto la funcion interna no forma parte del espacio global del programa, sino que queda limitada al ambito de la funcion exterior.
Esto se utiliza  para organizar mejor la logica del programa, ocultar detalles de implementacion o crear estructuras mas modulares.

## Argumento de una funcion
Los argumentos son los valores que se proporcionan a una funcion cuando esta es invocada, con el objeto de tranferir informacion al interior de la funcion para que puede operar sobre esos datos.

Desde un punto de vista conceptual, los argumentos representan el mecaniemo de comunicacion entre el exterior de la funcion y su contexto interno de ejecucion.

Cuando una funcion se ejecuta, se crea un entorno local en el que los valores de los argumentos se asocian a los paramentros definidos en la funcion.. Esta asociacion permite  que la logica interna de la funcion utilice esos valores para ralizar calculos, transformaciones o evaluaciones.

## Argumentos y parametros

**Parametros** son las variables definidas en la declaracion de la funcion. Actuan como contenedores que recibiran los valores cuando la funcion sea llamada.

**Argumentos** son los valores reales que se pasan a la funcion durante la llamada

En terminos teoricos:
- El parametro pertenece a la definicion de la funcion.
- El argumento pertenece a la invocacion de la funcion.


## Asociacion entre argumentosy parametros
Este proceso puede realizarse mediante distintos mecanismos, siendo los mas comunes por posicion y por nombre.

- **Por Posicion**
Los argumentos por posicion son aquellos que se asignan  a los paramentros de una funcion segun el orden en el que aparecen en la llamada.

La corrrespondencia entre argumentos y paramentros se basa exclusivamente en la posicion relativa dentro  de la lista de argumentos.Esto significa que:

    - El primer argumento se a asigna al primer paramentro
    - El segundo argumento al segundo parametro 
    - y asi sucesivamente.

Si se altera el orden, los valores pueden asociarse a parametros incorrectos, lo que puede modificar completamente el comportamiento de la funcion. Por ello se usa  cuando el numero de parametros es pequeño, el orden de los parametros es claro o cuando el significado de los valores es evidente.

En los parametros tambien podemos tener un paramentro opcional que tiene un valor asociado predeterminado de manera que la funcion puede ejecutarse aunque ese argumento no se proporcionado durante la llamada.

Se considera opcional cuando la funcion ddispones de un valor previamente definido que sera utilizado automaticamente si el usuario no pasa un argumento para ese paramentro.
El valor predeterminado se denomina valor por defecto.

El orden de los parametros es primero los obligatorios y luego los opcionales
´´´
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}!")

saludar('Keira')
´´´

- **Por** **nombre**
Los parametros por nombre (keywords arguments) permite asignar valores a los argumentos de funcion utilizando el nombre del parametro y en lugar de su posicion. Esto mejora la legibilidad, permit cambiar el orden de los argumentos y facilita la omision de parametros con valores predeterminados.

Al usar nombres el orden de los argumentos en la llamada no importa.
Usando un asterisco * en la definicion, se fuerza a que los parametros siguientes se pasen por nombre.

```
def funcion(*, a, b):
    return a + b
# funcion(1, 2) # Error
funcion(a=1, b=2) # Correcto

```
## *args y **kwargs (unpacking)
*arg permite a una funcion recibir un numero variable de argumentos posicionales, empaquetandolos automaticcamente en un tupla.

Se usa anteponiendo un arterisco (*) al nombre del parametro (convencionalmente args),
se puede usar cualquier nombre pero es de buenas practicas usar args.

Permite que  una funcion reciba desde cero hasta infinitos argumentos sin tener que definirlos todos explicitamente.

Es ideal cuando no sabes de antemano cuantos parametros pasara el usuario.

Evita la creacion de funciones sobrecargadas o con demasiados parametros opcionales.

De manera similar funciona **kwargs 

Kwargs es una convencion de python para empaquetar argumentos de  palabra clave (keyword arguments). En otras palabras para empaquetar diccionarios y funciona con cualquier nombre de variable siempre que se mantenga el doble arterisco (**) al principio, pero no es la conveccion y una buena practica para que el codigo sea legible.

Los argumentos pasados se reciben dentro de una funcion como un diccionario, donde las claves representan los nombre de los argumentos y los valores de los datos asociado, lo que permite iterarlos

** Join() con *args
El metodo join() pertenece al tipo cadena de texto(str) y se utiliza para concatenar multiples candenas en una sola.

Su funcionamiento es el siguiente, se toma la seucneca iterable de cadenas, se inserta entre ellas una cadena separadora y el resultado es una nueva cadena resultante.

Es importatnte entender que join() no concatena directamente argumentos individuales, sino que necesita una estructura iterable que contenga las cadenas

Dado que join() necesita precisamente un iterable de cadenas, la tupla generada por *args puede utilizarse directamente como entrada para join().

El funcionamiento es: El usuario pasa varios argumentos posicionales a la funcion, python los agrupa automaticamente en una tupla(args), esta tupla actua como secuencia de elementos, join() recorre esa secuenciay combina sus elementos en una sola cadena utilizando un separador.
```
def unir_lenguajes(*args):
    return (f'Los lenguajes de programacion son {", ".join(args)}')

resultado = unir_lenguajes("Python", "Java", "C++", "JavaScript")
print(resultado)

# natural language list formatting

def unir_lenguajes(*args):
    if len(args) == 1:
        lista = args[0]
    elif len(args) == 2:
        lista = " y ".join(args)
    else:
        lista = ", ".join(args[:-1]) + " y " + args[-1]

    return f"Los lenguajes de programación son {lista}"

resultado = unir_lenguajes("Python", "Java", "C++", "JavaScript")
print(resultado)

```
## Lambda
Una funcion lambda en python es un pequeña funcion anonima de una soloa linea definida sin nombre usando la palaba clave lambda en lugar de def.
Son ideales para tareas temporales, simples, y se usan comunmente como argumentos en funciones de orden superior como map(), filter() o sort().
Este tipo de funiones puedewn tomar cualquier numero de argumentos pero solo pueden tener una expresion.
Su sintaxis es:

- argumentos son los valores que recibe la funcion

- expresion es la operacion que se ejecuta y cuyo resultado se devuelve


```
lambda argumentos: expresion
```
La lambda no necesita return, porque el resultado se devuelve automaticamente

Una función lambda es una función anónima, es decir, una función que no tiene nombre y que se define utilizando la palabra clave lambda.

Desde el punto de vista conceptual, una lambda permite crear una función simple directamente en el lugar donde se necesita, sin tener que definirla previamente con def.

Se utilizan principalmente cuando la funcion es corta, solo se necesita una vez y se quier escribir el codigo de forma  mas compacta. A diferencia de las funciones normales devuelve automaticamente el resulta de esa expresion.
Las lambdas son útiles cuando:

 - la función es muy simple
 - se usa una sola vez
 - se necesita como argumento de otra función

Sin embargo, cuando la lógica es más compleja, es mejor usar funciones normales con def, porque son más claras y fáciles de mantener.

## Librerias

```
 CÓDIGO
   │
   ├── Built-in (print, format, len)
   │
   ├── Standard Library (math, datetime, os)
   │
   └── Third-party (numpy, requests, pandas)
            │
            └── PyPI (repositorio online)
                     │
                     └── pip (instalador)
```
