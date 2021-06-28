
import re
import html5lib
from requests import get
from bs4 import BeautifulSoup

titulos= set()

resposta = get("https://pt.wikipedia.org/wiki/Pain_Gaming")
tags = BeautifulSoup(resposta.text, "html5lib")

title = tags.find("title")
print(f"Página principal: {title}")

p = tags.find_all("p")

for i in p:
    anchors = i.find_all("a", href=re.compile("/wiki/"))
    for a in anchors:
        titulo = (a.get('title'))
        titulos.add(titulo)
        print(f"Página secundária: {titulo}.")


print(titulos)
   