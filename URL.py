import re
class URL:
    def __init__(self, pUrl):
        self.__url = self.higieniza_url(pUrl)
        
    #methods
    def higieniza_url(self, pUrl):
        if type(pUrl) == str:
            return pUrl.strip()
        else:  
            raise ValueError("É necessário informar um valor do tipo String(texto)")

    def valida_url(self):
        if not self.__url:  
            raise ValueError("A URL está vazia")
             
        padrao_url = re.compile('(http(s)?://)?(www.)?google.com(.br)?/search')
        match = padrao_url.match(self.__url)
        if not match:
            raise ValueError("A URL não é válida.")
        print("URL validada com sucesso!")
        return True
                
    #properties
    
    @property    
    def url_completa(self):
        return self.__url
    
    @property
    def url_base(self):
        if self.valida_url():
            separador = self.__url.find("?")
            url_base = self.__url[:separador]
            return "URL base: " + url_base
    
    @property
    def url_parametros(self):
        if self.valida_url():
            separador = self.__url.find("?")
            url_parametros = self.__url[(separador+1):]
            return "URL parâmetros: " + url_parametros