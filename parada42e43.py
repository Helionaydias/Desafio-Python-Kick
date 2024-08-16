# nota1  = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3  = float(input("Digite a terceira nota: "))

# media = (nota1 + nota2 +nota3)/3

# if media < 6 :
#   print("Aluno reprovado", media)
# else:
#     print("Aluno aprovado", media)


peso =  float(input("Digite seu peso: "))

altura =  float(input("Digite sua altura: "))

imc  = peso / (altura * altura)

if imc <  18.5:
  print("Magreza")
elif  18.5 <= imc <= 24.9:
  print("Normal")
elif  25 <= imc <= 29.9:
  print("Sobrepeso")
elif  30 <= imc <= 39.9:
  print("Obesidade")  
else:
  print("Obesidade grave")


# def calcular_imc(altura, peso):
#   imc = peso / (altura * altura)
#   return imc
# peso =  float(input("Digite seu peso: "))
# altura =  float(input("Digite sua altura: "))

# imc = calcular_imc(altura, peso)
# print(" Seu índice de Massa Corporal é ", imc)
  