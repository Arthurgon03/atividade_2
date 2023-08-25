peso=float(input("Qual seu peso em Kg: "))
altura=float(input("Qual sua altura em centímetros: "))
imc=0

altura_imc = altura/100

imc=(peso/altura_imc**2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III(Mórbida)")
