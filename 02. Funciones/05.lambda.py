# Funcion saludar
def greeting(first, last):
      print (f'Hola {first} {last}')


greeting('keira','McDowel')

# funcion Lambda

lambda first, last: (f'Hello {first} {last}')

# funcion lambda guardada en una variable

full_name = lambda first, last: f'again {first} {last}'

# Funcion lambda dentro de una funcion

def greeting_new(name):
      print (f'Hi there {name}')
      
      
greeting_new(full_name('Keira','McDowel'))


#Ejemplo con map()
#Transformar números multiplicándolos por 2:

numeros = [1, 2, 3, 4]

resultado = map(lambda x: x * 2, numeros)

print(list(resultado)) # [2, 4, 6, 8]


# Ejemplo con filter()
# Seleccionar números pares:

numeros = [1, 2, 3, 4, 5, 6]

pares = filter(lambda x: x % 2 == 0, numeros)

print(list(pares)) # [2, 4, 6]


# Ejemplo con sorted()
# Ordenar palabras por longitud:

palabras = ["python", "java", "go", "javascript"]

ordenadas = sorted(palabras, key=lambda palabra: len(palabra))

print(ordenadas)  # ['go', 'java', 'python', 'javascript']


