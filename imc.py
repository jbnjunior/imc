print("Calculadora de IMC - Índice de Massa Corporal")

peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Baixo peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso adequado")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação: Obesidade grau I")
elif 35 <= imc < 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")
