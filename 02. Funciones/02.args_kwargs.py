
def greeting(**kwargs):
  print(kwargs)


greeting()
greeting(first = 'Keira', last = 'McDowel')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Keira', last = 'McDowel')

def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'keira', 'McDowel',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')

def describir_lenguajes(tipo, *args, **kwargs):
    lenguajes = ", ".join(args)

    print(f"Tipo de lenguajes: {tipo}")
    print(f"Lenguajes: {lenguajes}")
    print("\nCaracterísticas:")

    for clave, valor in kwargs.items():
        print(f"{clave}: => {valor}")


describir_lenguajes(
    "Lenguajes populares",
    "Python", "Java", "JavaScript",
    tipado="dinámico o estático",
    uso_principal="desarrollo web y software",
    paradigma="orientado a objetos y funcional"
)




def unir_lenguajes(*args):
    return (f'Los lenguajes de programacion son {", ".join(args)}')

resultado = unir_lenguajes("Python", "Java", "C++", "JavaScript")
print(resultado)


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