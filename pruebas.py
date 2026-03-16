

def unir_lenguajes(*args):
    return (f'Los lenguajes de programacion son {", ".join(args)}')

resultado = unir_lenguajes("Python", "Java", "C++", "JavaScript")
print(resultado)
