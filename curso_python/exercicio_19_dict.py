nome = input("Forneça seu nome: ")
idade = int(input("Forneça sua idade: "))
telefone = input("Forneça seu telefone: ")
endereco = input("Forneça seu endereço: ")

pessoa = {
    "nome": nome,
    "idade": idade,
    "telefone": telefone,
    "endereco": endereco
}

for p, v in pessoa.items():
    print(f"Chave: {p} - Valor: {v}")