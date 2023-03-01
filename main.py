from URL import URL
url_google = URL('https://www.google.com/search?q=gerador+de+cpf&source=hp&ved=0ahUKEwibtOCXg7v9AhXCArkGHW2ECwEQ4dUDCAg&oq=gerador+de+cpf')
print(url_google.url_base)
print(url_google.url_parametros)
print(url_google.get_valor_parametro("q"))
print(url_google.get_valor_parametro("source"))
print(url_google.get_valor_parametro("ved"))
print(url_google.get_valor_parametro("oq"))
print(url_google)

#tests

##url_vazia = URL("   ")
##url_vazia.valida_url()
##url_numerica = URL(123)
