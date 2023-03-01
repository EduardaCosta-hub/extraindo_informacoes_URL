from extrator_url import ExtratorURL
url = 'https://www.google.com/search?q=gerador+de+cpf'
url_extraida = ExtratorURL(url)
print(url_extraida.url)
url_extraida.valida_url()
'''separador = url.find("?")
url_base = url[:separador]
url_parametros = url[separador+1:]
print(url)
print(url_base)
print(url_parametros)'''