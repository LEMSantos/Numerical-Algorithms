# coding: utf-8
import numpy

def calculateStep(a, b, n):
    return (b-a)/n # retorna o valor de h, onde a é o limite inferior, b o superior e n é a quantidade de intervalos


def trapezeRule(step, data):
    return (step/2) * (data[0] + 2 * sum(data[1:-1]) + data[-1]) #Calcula o método utilizando h/2 * (y0 + (y1 + y2 + y3 + ... + yn-1) + yn)

def simpsonByThree(step, data):
    even = [data[i] for i in range(2,len(data) - 1, 2)] #Separa os números que estão nos índices pares do vetor de valores
    odd = [data[i] for i in range(1,len(data) - 1, 2)]  #Separa os números que estão nos índices ímpares do vetor de valores

    return (step/3) * (data[0] + 4 * sum(odd) + 2 * sum(even) + data[-1]) #Calcula o método utilizando a fórmula h/3 * (y0 + 4 * (y1 + y3 + y5 + ... + y2n-1) + 2 * (y2 + y4 + y6 + ... + y2n) + yn)

option = 0
i = 0
j = 0
k = 0

while (k == 0):

    while (i == 0):
        i = int(input("\nEntre com 1 para calcular a partir de uma funcao f(x) e limites\nEntre com 2 para calcular a partir de uma tabela de dados\nSua opcao: "))
        if i == 1:
            a = float(input("\nEntre com o limite inferior: "))
            b = float(input("Entre com o limite superior: "))
            interval = float(input("Entre com o numero de intervalos desejados: "))
            func = input("Entre com a funcao desejada no seguinte formato - lambda x: f(x) \n-> ")
            funcFinal = eval(func)
            step = calculateStep(a, b, interval)
            values = [funcFinal(i) for i in numpy.arange(a, b + step, step)]
        elif i == 2:
            step = float(input("Insira o valor do passo: "))
            print("Insira os valores de f(x) separados por espaco: ")
            values = list(map(float,input().split()))
        else:
            i = 0
        
    while(j == 0):
        j = int(input("\nEntre com 1 para o metodo do trapezio\nEntre com 2 para 1/3 de Simpson\nSua opcao: "))
        if j == 1:
            option = 1
        elif j == 2:
            option = 2
        else:
            j = 0

    if option == 1:
        print("\n\nO resultado da integral definida pelo metodo dos trapezios para %d intervalos e f(x) ou tabela fornecidos sera\n-> %.6f" % ((len(values) -1 ), trapezeRule(step, values)))
    else:
        print("\n\nO resultado da integral definida pelo metodo de 1/3 de Simpson para %d intervalos e f(x) ou tabela fornecidos sera\n-> %.6f" % ((len(values) -1 ), simpsonByThree(step, values)))

    if k == 0:
        x = int(input("\n\nDeseja calcular uma nova integral?\n1 - Sim, calcular outra integral\n2 - Encerrar o programa\nInsira sua opcao: "))
        if x == 1:
            i = 0
            j = 0
            k = 0
        else:
            k = 1
