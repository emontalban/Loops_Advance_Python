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

For .. in permite itera sobre cada elemento de una sestructura de datos, un iterable es cualquier objeto que pueda recorrerse elemento por elemento como listas, tuplas sets, diccionarios, strings, rangos

### Funcionamiento conceptual
```
colección de datos

[elemento1, elemento2, elemento3]

for elemento in colección:

    ejecutar código
```
