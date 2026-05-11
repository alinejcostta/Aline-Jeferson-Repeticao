
# QUESTÃO 25

# 25. Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.


soma = 0
pessoas = int(input("Digite quantas pessoas fazem parte da turma: "))

for i in range(pessoas):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    soma += idade

media = soma/pessoas

if media > 0 or media <= 25:
    print(f"A turma é jovem! Sua média de idade é {media}")
elif media > 26 or media <= 60:
    print (f"A turma é adulta! Sua média de idade é {media}")
elif media > 60:
    print(f"A turma é idosa! Sua média de idade é {media}")
else:
    print("Houve algum erro durante o preenchimento, tente novamente.")