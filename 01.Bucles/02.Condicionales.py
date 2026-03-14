# Condicionales con if
edad = 18

if edad >= 18:
    print("Eres mayor de edad")

# condicion if..... else...
numero = 3

if numero > 5:
    print("Mayor que 5")
else:
    print("Menor o igual a 5")

# Operador ternario

edad = 20

mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"

print(mensaje)

# El operador ternario se puede usar entro de expresionesnumero = 7
numero =7
resultado = "par" if numero % 2 == 0 else "impar"

print(resultado)

# operador ternario en listas
numbers = [1,2,3,4]

result = ["par" if n % 2 == 0 else "impar" for n in numbers]
print(result)

#Operador IN
frutas = ["manzana", "pera", "naranja"]

if "pera" in frutas:
    print("La pera está en la lista")

# operadores logicos
# and
edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes entrar al evento")

# or

dia = "sabado"

if dia == "sabado" or dia == "domingo":
    print("Es fin de semana")

#operador not

usuario_logueado = False

if not usuario_logueado:
    print("Debes iniciar sesión")

## Condicionales compuestos
edad = 25
tiene_entrada = True
vip = False

if edad >= 18 and (tiene_entrada or vip):
    print("Puedes entrar al concierto")

# operador empaquetar *

first, *middle, last = [1,2,3,4,5]

first = 1
middle = [2,3,4]
last = 5