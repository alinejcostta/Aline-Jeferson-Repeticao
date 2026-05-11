
# QUESTÃO 26

# 26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.


contador1 = 0
contador2 = 0
contador3 = 0

qtd_eleitores = int(input("Digite quantos eleitores irão votar: "))

for i in range(1, qtd_eleitores+1):
    voto = int(input("Vote no candidato desejado (1, 2 ou 3): "))

    if voto == 1:
        contador1 += 1
    elif voto == 2:
        contador2 += 1
    elif voto == 3:
        contador3 += 1
    else:
        print("Voto inválido!")

print(f"""
------ RESULTADO DA ELEIÇÃO ------
    Candidato 1: {contador1} votos
    Candidato 2: {contador2} votos
    Candidato 3: {contador3} votos
""")
