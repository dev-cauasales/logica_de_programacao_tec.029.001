# TODO: Crie um programa que receba do usuario um valor da gasolina e do etanol, e informe para o usuario qual o melhor combustivel para abastercer
#NOTE: compensa mais abastecer com etanol caso o valor do etanol corresponda a até 75% do valor da gasolina
#NOTE: e nao se esqueça do detalhe mais importante de todas:

#entrada de dados
gasolina = float(input("informe o valor da gasolina:").replace(",","."))
etanol =float(input("Informe o etanol:").replace(",","."))

#processamento de dados
if etanol <= gasolina *0.75:
 print ("Abasteça com etanol")
else:
 print ("Abasteça com gasolina")

