def full_name(first, last):
  print(f'{first} {last}')

full_name('keira','McDowel')


def auth(email, password):
  if email == 'email@email.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('email@email.com', 'asdf')

#parametros por nombre
def languages( name, age):
  print(f'El lenguaje de programacion {name} se creo en el año {age}')


languages(name = 'Python', age=1989)
languages('Go', 2009)

# parametros obligado a pasar los argumentos con nombre
def languages(*, name, age):
  print(f'El lenguaje de programacion {name} se creo en el año {age}')


languages(name = 'Python', age=1989)
languages('Go', 2009) # da error