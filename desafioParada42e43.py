
#Faça um programa em que o usuário digita dois valores e o resultado da soma é exibido na tela.​
valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))

resulta_soma = valor1 + valor2

print("A soma dos valores é : ", resulta_soma)

#Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. Depois mostre os valores digitados na tela.​
nome = input("Digite seu nome: ")
idade =  input("Digite sua idade: ")
telefone = input("Digite seu telefone: ")
email =  input("Digite seu email: ")

print(f" nome: {nome} idade: {idade} telefone: {telefone} email: {email}" )
#///////////////////////////////////////////////////

# Faça um programa no qual o usuário precisa cadastrar as informações de um produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra.​

codigo = int(input("Cadastre o código do produto : "))
nome = input("cadastre o nome do produto : ")
quantidade = int(input("cadastre a quantidade de produtos : "))
preco  = float(input("Cadastre os preços dos produtos : "))

valor_total = quantidade * preco

print(f" codigo: {codigo} nome: {nome} quantidade :{quantidade} preco: R${preco} valor Total da compra: R${valor_total:}")
#/////////////////////////////////////////

#Faça um programa que converte centímetros em metros.​
valor = float(input("Digite quantos centímetros você quer: "))
resultado = valor / 100
print("O resultado em metros é :", resultado)
#///////////////////////////////////////////////////

#Faça um programa que calcule a área de um quadrado/retângulo. ​
def calcular_area(  valor_b, valor_h):

  area = valor_b * valor_h
  return area

valor_b = float(input("Digite a base"))
valor_h = float(input("Digite a altura"))
area = calcular_area(valor_b, valor_h)
print(f"A área do retângulo de base {valor_b} e  altura {valor_h} é : {area}" )
  


