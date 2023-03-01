from URL import URL
url_google = URL('https://www.google.com/search?q=gerador+de+cpf')
print(url_google.url_base)
print(url_google.url_parametros)

#tests

##url_vazia = URL("   ")
##url_vazia.valida_url()
##url_numerica = URL(123)
