#entrada de dados
nome = input("nome:").strip().title()
nota1 = int(input("Informe a 1ª nota:"))
nota2 = int(input("Informe a 2ª nota:"))

#processamento de dados
media = (nota1+nota2)/2

#exibir a media
print(f"Media: {media}")

#estrutura de decisão
if media >= 7:
    print(f"{nome} está aprovado.")
elif media >= 5:
    print(f"{nome} está aprovado")
else:
    print(f"{nome} está aprovado")
    
