nome = input("Por favor forneça o seu nome: ")
idade = int(input("Por favor forneça a sua idade: "))
resp = input("Você possui curso superior?\n1- Sim\n2- Não\n")

tem_superior = None

if resp == '1':
    tem_superior = True
else: 
    tem_superior = False

print(f"Nome: {nome} - Idade: {idade} - Tem curso superior: {tem_superior}")
