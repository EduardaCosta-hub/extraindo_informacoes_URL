url = "http://insoft-lnx13:8080/akitasoft/app/?lang=pt_BR&theme=classic"
separador = url.find("?")
url_base = url[:separador]
url_parametros = url[separador+1:]
print(url)
print(url_base)
print(url_parametros)