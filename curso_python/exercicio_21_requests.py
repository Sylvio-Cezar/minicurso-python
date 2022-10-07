from urllib import response
import requests

cep = input("Forneça seu CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if (response.status_code == 200):
    print(f"O CEP: {cep} é válido")
else:
    print(f"O CEP: {cep} é inválido")

print(response.text)