import math

def calcular_imc(peso, altura):
    imc = peso / math.pow(altura, 2)
    return imc

def pegar_dados():
    peso = float(input("Insira o peso: "))
    altura = float(input("Insira a altura: "))
    return peso, altura

def main():
    p, a = pegar_dados()
    imc = calcular_imc(p, a)

    print(f"Com o peso: {p} KG e altura: {a} --> O seu IMC é de {imc}")

if __name__ == "__main__":
    main()
