
def hundred():
  for num in range(1, 101,2):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(11)


# funciones anidades



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


# Problemas con la mutabilidad o inmutabilidad

def some_function(collection = []): 
  collection.append(1) 
  print(id(collection)) 
  return collection 

print(some_function())  # [1]
print(some_function())  # [1,1]

## como la lista ya existe añada no crea una nueva para evitar este tipo de situaciones

def some_function(collection=None):
    if collection is None:
        collection = []
    collection.append(1)
    return collection

print(some_function())
print(some_function())
