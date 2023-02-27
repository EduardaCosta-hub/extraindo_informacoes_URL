from extrator_url import ExtratorURL
url = 'https://www.w3schools.com/python?'
separador = url.find("?")
url_base = url[:separador]
url_parametros = url[separador+1:]
print(url)
print(url_base)
print(url_parametros)