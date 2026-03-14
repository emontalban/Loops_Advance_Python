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

### Braak y Continue
#### Break
Break es la palabra clave que permite interrumpir inmediatamente un bucle, el proposito es salir del bucle cuando se 
cumple la condicion especifica, un uso tipico es detener el bucle  al encontrar un valor buscado o evitar procesamiento adicional
cuando ya se alcanzo el objetivo.
Break detiene el bucle por completo incluso si todavia qudan elementos por iterar. 

#### Continue
Continue  es una palabra clave que permite saltar la iteracion actual de un bucle y continuar con la siguiente iteracion. 
Omite ciertas iteraciones que cumplen una condicion, sin deterner el bucle completo. Se usa para saltar elementos no deseados e ignorar
casos especificos mientras se sigue procesando el resto de la secuencia.
Continue no termina el bucle, solo omite la iteracion actual.

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
- 1. El valor que se devuelve si la condicion es verdadera
- 2. La conddicion que se evalua
- 3. El valor que se devuelve si la condicion es falsa.

Su objetivo principal es simplificar expresiones condicionales simples, haciendo el codigo mas compacto y legible cuando solo se necesita elegir entre dos resultados.

valor_si_true if condicion else valor_si_false

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

#### And
El operador and se utiliza para combinar dos o mas condicionales y el resultado sera True unicamente si todas las condiciones evaluadas son verdaderas.

```

| Condición A | Condición B | Resultado |
|-------------|-------------|-----------|
| True        | True        | True      |
| True        | False       | False     |
| False       | True        | False     |
| False       | False       | False     |
```

```
## Operador lógico `or`

| Condición A | Condición B | Resultado |
|-------------|-------------|-----------|
| True        | True        |      True |
| True        | False       |      True |
| False       | True        |      True |
| False       | False       |     False |

```

```
## Operador lógico `not`

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