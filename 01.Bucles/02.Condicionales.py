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