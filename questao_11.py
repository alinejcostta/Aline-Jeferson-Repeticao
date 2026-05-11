
# QUESTÃO 11

# 11. Altere o programa anterior para mostrar no final a soma dos números.

soma = 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

menor = min(num1, num2)
maior = max(num1, num2)

for i in range(menor, maior+1):
    soma += i
    print(i)

print(f"A soma dos números é {soma}")
