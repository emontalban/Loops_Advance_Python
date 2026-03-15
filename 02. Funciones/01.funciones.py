def full_name(first, last):
  print(f'{first} {last}')

full_name('keira','McDowel')


def auth(email, password):
  if email == 'email@email.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('email@email.com', 'asdf')

def hundred():
  for num in range(1, 101):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)

# Ejemplo de utiliza *args, **kwargs

def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')

# # funciones anidades
# def Sumar(sumando1, sumando2):
#   return sumando1 + sumando2

# def Restar(minuendo, sustraendo):
#   return minuendo - sustraendo

# numero1 = int(input('Introduce el primer numero'))
# numero2 = int(input('Introduce el segundo numero'))

# resultado_suma, resultado_resta = SumarRestar(numero1, numero2)

def SumarRestar(param1, param2):
  return Sumar(param1, param2), Restar(param1, param2)

def Sumar(sumando1, sumando2): 
  return sumando1 + sumando2 

def Restar(minuendo, sustraendo): 
  return minuendo - sustraendo

numero1 = int(input("Introduce el primer numero: ")) 
numero2 = int(input("Introduce el segundo numero: ")) 

resultadosuma, resultadoresta = SumarRestar(numero1,numero2) 
print("El resultado de la suma es: ", resultadosuma) 
print("El resultado de la resta es: ", resultadoresta)