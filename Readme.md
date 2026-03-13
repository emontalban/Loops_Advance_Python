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