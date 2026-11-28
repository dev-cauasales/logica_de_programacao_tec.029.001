#TODO: Crie im programa que receba do usuario o nome, a massa e a altura, e calculeseu IMC( indice da massa corporal).Apos mostrar o IMC, o programa deve informar de acordo com o valor do seu IMC:
# IMC < 18,5: "Usuario esta abaixo do peso"
# IMC < 25: "Usuario esta no peso ideal"
# IMC < 30: "Usuario está acima do peso"
# IMC < 35: "Usuario esta obeso"
# IMC < 40: "Usuario esta com obesidade nivel 2"
# Se nao estiver em nenhum dos casos acima: "Usuario esta com obesidade morbida"

#entrada de dados
nome = input("nome:").strip().title()
massa = float(input("massa:").replace(",","."))
altura = float(input("altura:").replace(",","."))

#saida de dados
imc = massa / (altura **2)
print(f"IMC: {imc:.2f}")
if imc < 18.5:
 print(f"{nome} você está abaixo do peso")
elif imc < 25:
 print(f"{nome} você está no peso ideal")
elif imc < 30:
 print(f"{nome} você está acima do peso")
elif imc < 35:
 print(f"{nome} você está obeso")
elif imc < 40:
 print(f"{nome} você está com obesidade nivel 2")
else:
 print (f"{nome} você está com obesidade morbida")

