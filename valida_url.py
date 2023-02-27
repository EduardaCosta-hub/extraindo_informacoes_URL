def valida_url(self):
    if not self.url:  # Essa validação já existia
        raise ValueError("A URL está vazia")

    padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
    match = padrao_url.match(self.url)
    if not match:
        raise ValueError("A URL não é válida.")