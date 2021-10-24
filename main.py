# encutando endereços web
# usando a biblioteca pyshorteners

import pyshorteners 

url_endereco = "https://www.youtube.com/watch?v=mQSVKCmeAQE&list=PLf1lowbdbFIAURvpD8Qy8PqwrMjwx0N64"

link_endereco = pyshorteners.Shortener()

shorten_url_endereco = link_endereco.tinyurl.short(url_endereco)

print(shorten_url_endereco)

#passo1 - importar a biblioteca pyshorteners
#passo2 - criar uma variavel pra url
#passo3 - criar uma variavel para a biblioteca pyshorteners
#passo4 - criar uma variavel para o tinyurl
#passo5 - print da ultima variavel
