aux = 0.9144
str = "Fim do Programa"

def soma(a: int, b: int) -> int:
    return a + b

def subt(a: int, b: int) -> int:
    return a - b

def mult(a: int, b: int) -> int:
    return a * b

def divi(a: int, b: int) -> float:
    return a / b

def temperature(a: float) -> float:
    return (a * (9/5)) + 32

def distance(a: int) -> int:
    return (a / aux)

def volume(a: float) -> float:
    return a * 1000

def weigth(a: float) -> float:
    return (a * 2.205)

def imc(a: float, b: float) -> float:
    return (a / (b*b))



if __name__ == '__main__':

    option = int(input("Digite uma opção \n"
                   "1 - Calculadora \n"
                   "2 - Conversão \n"
                   "3 - IMC \n"
                   "4 - Sair\n"))

    if option == 1:
        calc = int(input("Digite uma opção \n"
                   "1 - Soma \n"
                   "2 - Subtração \n"
                   "3 - Multiplicação \n"
                   "4 - Divisão\n"))

        a = int(input("Digite o primeiro número \n"))
        b = int(input("Digite o segundo número \n"))

        if calc == 1:
            print("A soma é igual {}" .format(soma(a, b)))
        elif calc == 2:
            print("A subtração é igual {}".format(subt(a, b)))
        elif calc == 3:
            print("A multiplicação é igual {}".format(mult(a, b)))
        elif calc == 4:
            print("A divisão é igual {}".format(divi(a, b)))
        else:
            print(str)
        print(str)
    elif option == 2:
        converter = int(input("Digite uma opção \n"
                     "1 - Temperatura \n"
                     "2 - Distância \n"
                     "3 - Volume \n"
                     "4 - Peso\n"))

        a = float(input("Digite  o valor para conversão\n"))

        if converter == 1:
            print("{0}°C em Farenheit é igual a {1}".format(a, temperature(a)))
        elif converter == 2:
            print("{0} metros em milhas é igual a {1}".format(a, distance(a)))
        elif converter == 3:
            print("{0} litros em  mililiro(s) é igual a {1}".format(a, volume(a)))
        elif converter == 4:
            print("{0}Kg em libra é igual a {1}".format(a, weigth(a)))
        else:
            print(str)
        print(str)
    elif option == 3:
        peso = float(input( "Digite seu peso \n"))
        altura = float(input ("Digite sua altura \n"))

        print("{0}Kg multiplicando com {1}m ao quadrado da o imc de {2}".format(peso, altura, imc(peso, altura)))
        print(str)
    else:
        print(str)