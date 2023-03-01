import re
class URL:
    def __init__(self, pUrl):
        self.__url = self.higieniza_url(pUrl)
        
    #methods
    def higieniza_url(self, pUrl):
        if type(pUrl) == str:
            return pUrl.strip()
        else:  
            return ValueError("É necessário informar um valor do tipo String(texto)")
    def valida_url(self):
        url = self.__url
        print(url)
        if not url:  
            raise ValueError("A URL está vazia")
             
        padrao_url = re.compile('(http(s)?://)?(www.)?google.com(.br)?/search')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")
        print("URL validada com sucesso!")
    
    #properties
    
    @property    
    def url(self):
        return self.__url
