import re
class ExtratorURL:
    def __init__(self, purl):
        self.__url = purl.strip
        print(purl)
        print(self.__url)

    def valida_url(self):
        url = self.__url
        print(url)
        if not url:  
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?w3schools.com(.br)?/python')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")
        print("URL validada com sucesso!")

    def get_url_base(self):
        """Retorna a base da url."""
        ...

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        ...

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
