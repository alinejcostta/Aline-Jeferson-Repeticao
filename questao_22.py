
# QUESTÃO 22

# 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.


divisores = []
numero = int(input("Digite um número inteiro: "))

primo = True

for i in range (2, numero):
    if numero % i == 0:
        primo = False
        divisores.append(i)
        break

if primo:
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo!")
    print(f"Ele é divisível por: {divisores}")