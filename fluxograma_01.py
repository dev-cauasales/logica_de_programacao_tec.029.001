# entrada de dados
nome = input("Informe o nome: ").strip().title()
email = input("Informe o e-mail: ").strip().lower()
cpf = input("Informe o CPF: ").strip()
telefone = input("Informe o telefone: ").strip()
idade = int(input("Informe a idade: "))
altura = float(input("informe sua altura: ").replace(",", "."))

#saida de dados
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros")

