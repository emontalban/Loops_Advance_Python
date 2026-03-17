import requests
from bs4 import BeautifulSoup
from inflection import titleize

""" def obtener_titulos():
    # 1. URL de la web
    url = "http://books.toscrape.com/"
   

    # 2. Hacer petición HTTP
    response = requests.get(url)
    html = response.text

    # 3. Parsear HTML
    soup = BeautifulSoup(html, "html.parser")

    # 4. Buscar todos los enlaces
    links = soup.find_all("a")

    # 5. Filtrar enlaces válidos
    filtered_links = []

    for link in links:
        href = link.get("href")

        if href and "catalogue" in href:
            filtered_links.append(href)

     # 6. Eliminar duplicados
    filtered_links = list(set(filtered_links))

    # 7. Convertir URLs a títulos
    titulos = []

    for link in filtered_links:
        # coger la parte importante de la URL
        slug = link.split("/")[-2]

        # eliminar números
        palabras = slug.split("-")
        palabras = [p for p in palabras if not p.isdigit()]

        # unir y formatear
        texto = " ".join(palabras)
        titulo = titleize(texto)

        titulos.append(titulo)

    return titulos


# Ejecutar función
resultado = obtener_titulos()

for titulo in resultado:
    print(titulo) """


def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'catalogue' in url:
            url = url.split('/')[-2]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

# UPDATED CODE
    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))
# UPDATED CODE

    return titles


r = requests.get("http://books.toscrape.com/")
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:
    print(title)


url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# NUEVO selector correcto
links = soup.select(".titleline > a")

for link in links:
    print(link.text)
    print(link.get("href"))
    print("-----")