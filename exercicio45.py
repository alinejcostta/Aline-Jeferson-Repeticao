
# QUESTÃO 45

# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

questoes_certas = 0

maior_acerto = float("-inf")
nome_maior_acerto = ""

menor_acerto = float("inf")
nome_menor_acerto = ""

qtd_provas = 0

soma_notas = 0
media_notas = 0

while True:
    nome = input("Digite o seu nome:")

    q1 = input("Digite a resposta da questão 1: ")
    if q1 == "A":
        questoes_certas += 1

    q2 = input("Digite a resposta da questão 2: ")
    if q2 == "B":
        questoes_certas += 1

    q3 = input("Digite a resposta da questão 3: ")
    if q3 == "C":
        questoes_certas += 1

    q4 = input("Digite a resposta da questão 4: ")
    if q4 == "D":
        questoes_certas += 1

    q5 = input("Digite a resposta da questão 5: ")
    if q5 == "E":
        questoes_certas += 1

    q6 = input("Digite a resposta da questão 6: ")
    if q6 == "E":
        questoes_certas += 1

    q7 = input("Digite a resposta da questão 7: ")
    if q7 == "D":
        questoes_certas += 1

    q8 = input("Digite a resposta da questão 8: ")
    if q8 == "C":
        questoes_certas += 1

    q9 = input("Digite a resposta da questão 9: ")
    if q9 == "B":
        questoes_certas += 1

    q10 = input("Digite a resposta da questão 10: ")
    if q10 == "A":
        questoes_certas += 1

    nota = questoes_certas
    print(f"Questões corretas: {questoes_certas}")
    print(f"Nota: {nota:.1f}")

    soma += nota

    qtd_provas += 1

    if questoes_certas > maior_acerto:
        maior_acerto = questoes_certas
        nome_maior_acerto = nome

    if questoes_certas < menor_acerto:
        menor_acerto = questoes_certas
        nome_menor_acerto = nome

    resposta = input("Outro aluno irá realizar a prova? (S/N)")

    if resposta == "N":
        break
    else:
        questoes_certas = 0

print(f"""
    Aluno com maior número de questões corretas: {nome_maior_acerto} ({maior_acerto})
      
    Aluno com menor número de questões corretas:{nome_menor_acerto} ({menor_acerto})
      
    Provas realidadas: {qtd_provas}
    
    Média da turma: {media_notas}
      """)
