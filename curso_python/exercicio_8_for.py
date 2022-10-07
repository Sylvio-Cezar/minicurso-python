valores_impar = list()

for n in range(100, 200):
    if n % 2 != 0:
        valores_impar.append(n)

for i, v in enumerate(valores_impar):
    print(f"Elemento {i} - Valor: {v}")
