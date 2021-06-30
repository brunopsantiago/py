lista = [1, 2, 3, 4, 5, "Oi", False]

tupla = (0, 2, 3, 4, 5, 9, "Ola", False)

lista.append(7)
print(lista)
lista.remove(5)
print(lista)

if 9 in lista or 9 in tupla:
    print("OK")
else:
    print("NOK")

lista = [1, 2, 3, 4, 5, "Oi", False]
tupla = (1, 2, 3, 4, 5, "Ola", False)
tupla2 = (1, 2, 3, 4, 5, "Oi", False)

if lista == tupla:
    print("lista igual a tupla")
elif lista == tupla2:
    print("lista igual a tupla 2")
else:
    print("Lista não é igual a nenhuma tupla")
print(type(lista))
print(type(tupla))
print(type(tupla2))
