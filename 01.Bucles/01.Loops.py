# Uso de for en listas y tuplas es igual

languages =["Python", "Rust", "Go", "JavaScript", "TypeScript", "Ruby"]

for language in languages:
    print(language)    

# El uso de for en diccionarios

programming_languages = {
    "Python":  "Guido van Rossum",
    "JavaScript": "Brendan Eich",
    "C": "Dennis Ritchie",
     "Rust":  "Graydon Hoare",
     "Java" : "James Gosling",   
     "C++":  "Bjarne Stroustrup"
    }
    
for language, creator in programming_languages.items():
    print ('Lenguaje', language)
    print('Creador', creator)

# con strings

alphabet = 'abcdef'

for letter in alphabet:
  print(letter)

#con rangos de numeros

for num in range(1, 10):
   print(num) # devolvera del uno al al 9 ya que el ultimo numero lo ignora

for num in range(1,10,2):
   print(num) # devolvera del dos en dos del uno al 9

# print del 1 al 10 usando while
nums = list(range(1,10))
while len(nums) > 0:
   print(nums.pop())



for language in languages:
   if language  == "Go":
      print (f'Sorry {language} is not implemented here')
      continue
   else:
      print (f'{language} is implemented')

# En este ejemplo vamos a buscar un elemento y cuando lo encontramos se acabo

for language in languages:
   if language  == "Go":
      print (f'{language} was found at index {languages.index(language)}')
      break
   
   print (language)

# como unir dos listas

old_users = ["Alice", "Bob", "Charlie"]
new_users = ["David", "Eve", "Frank"]
all_users = old_users + new_users

print(all_users)

# tambien podemos usar append()
for old_user in old_users:
   new_users.append(old_user)
print(new_users)

# listas compresivas

num_list = range(1, 11)
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

# segundo ejemplo con listas compresivas


even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)

num_list = range(1, 11)

even_number = [num  for num in num_list if num % 2 == 0]

print(even_number)