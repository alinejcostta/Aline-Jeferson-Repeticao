
# QUESTÃO 10

# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

menor = min(num1, num2)
maior = max(num1, num2)

for i in range(menor, maior+1):
    print(i)