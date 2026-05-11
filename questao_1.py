
# QUESTÃO 1

# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


quant_notas = int(input("Digite quantas notas deseja inserir: "))
soma = 0

for i in range(quant_notas):

    while True:
        nota = float(input("Digite uma nota de 0 a 10: "))

        if nota < 0 or nota > 10:
            print("Nota inválida!")

        else:
            soma += nota
            break

media = soma/quant_notas

print(f"A média é {media:.2f}")