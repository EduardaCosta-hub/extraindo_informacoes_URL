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
        return True
    
    #getters and setters
    
    def get_valor_parametro(self, pNome_parametro):
        indice_parametro = self.url_parametros.find(str(pNome_parametro))
        indice_valor = indice_parametro + len(str(pNome_parametro)) + 1
        indice_e_comercial = self.url_parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros[indice_valor:]
        else:
            valor = self.url_parametros[indice_valor:indice_e_comercial]
        return "O valor do parâmetro "+ pNome_parametro + " é " + valor
               
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