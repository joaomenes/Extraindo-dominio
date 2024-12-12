import re

url = r"(?<=https://www.)([^.]+)"
link = "https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python"

resultado = re.search(url, link)

if resultado:
    dominio = resultado.group(1)
    print(dominio) 
else:
    print("Domínio não encontrado")