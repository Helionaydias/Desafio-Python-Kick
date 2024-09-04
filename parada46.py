# def soma_numeros(a, b):
#   return a + b

# result = soma_numeros(8,3)
# print(result)


# /////////////////////

# def eh_par(numero):
#   if numero % 2 == 0:
#     print(f"O número {numero} é par ")
#     return True
#   else:
#     print(f"O número {numero} é impar")
#     return False

# eh_par(2)
# eh_par(3)    
  

# def reverter_string(texto):
#   return texto[::-1]
# resultado= reverter_string("Python")
# print(f" {resultado}")

# def contar_vogais(texto):
#   vogais = ['a', 'e', 'i', 'o', 'u']
#   if texto.lower() in vogais:
#     return True
#     vogais.count('a', 'e', 'i', 'o', 'u')
#   else:  
#     return False
# resultado = contar_vogais("Programação")  
# print(resultado)
def conta_vogais(string):
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    vogais = 'aeiou'
    return sum(string.count(i) for i in vogais)

print(conta_vogais('olaaa'))
  
