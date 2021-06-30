# Construir uma condição para verificar se o número é múltiplo de 3.
num = 9

resultado = 120 % 3

if resultado == 0:
    print("Numero digitado é múltiplo de 3")
    print(resultado)
else:
    print("Não é múltiplo")
    print(resultado)

# Crie 3 condicionais utilizando a estrutura elif.
lista = [1, 2, 3, 4, 5, "Oi", False]
tupla = (0, 2, 3, 4, 5, "Ola", False)

lista.append(7)
print(lista)
lista.remove(1)
print(lista)

if 9 in lista or 9 in tupla:
    print("9 em alguma das estrutas")
elif 9 in lista and 0 in tupla:
    print("9 e 0 não estão nas duas estruturas, respectivamente")
else:
    print("else")

# Crie uma lista e verifique se ela contém os números 7 e 3.
lista2 = [1, 2, 4, 5, "Oi", False]
if 3 in lista2 and 7 in lista2:
    print("3 e 7 estão na lista")
elif 3 in lista2 or 7 in lista2:
    print("3 ou 7 estao na lista")
else:
    print("3 e 7 nao estao na lista")

# Crie uma lista com 5 valores e uma tupla com 10 valores, verifique se algum valor da lista está contido na tupla.
# exercicio incompleto (todos os valores da lista estao na tupla, mas da erro)
# como verifica todos os elementos da lista de uma vez?
lista5 = [1, 2, 3, 4, 5]
tupla5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, "Oi")

if lista5 in tupla5:
    print("Valores da lista estao na tupla")
else:
    print("Valores nao estao na tupla")
