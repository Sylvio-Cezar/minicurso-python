from datetime import date

ano = int(input("Forneça o ano: "))
mes = int(input("Forneça o mês: "))
dia = int(input("Forneça o dia: "))

hoje = date.today()
nascimento = date(ano, mes, dia)

resultado = hoje - nascimento

print(f"Você tem o total de {resultado.days} dias")