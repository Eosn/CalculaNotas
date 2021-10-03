'''
Éllen Oliveira Silva Neves (20202BSI0071)
Trabalho solicitado pelo professor da disciplina de Programação II, Hilário Seibel Junior
'''

import pickle
import os


def infoAluno(tupla, alunos):  # coloca as informações relevantes p/ comparação em uma tupla
    matricula = tupla[0]
    nome = alunos[matricula]
    nota2 = tupla[2]
    tempo = tupla[5]
    notaTotal = tupla[1] + tupla[2] + tupla[3] + tupla[4]
    return (nome, nota2, tempo, notaTotal)


def anterior(x, y):  # aluno1, aluno2
    if x[3] > y[3]:  # compara nota total
        return True
    if x[3] < y[3]:
        return False

    if x[1] > y[1]:  # compara nota 2
        return True
    if x[1] < y[1]:
        return False

    if x[2] < y[2]:  # compara tempo de execução
        return True
    if x[2] > y[2]:
        return False

    if x[0] < y[0]:  # compara ordem alfabética
        return True
    if x[0] > y[0]:
        return False
    return None


def mergeSort(notas, alunos):
    if len(notas) > 1:
        meio = len(notas) // 2
        lEsq = notas[:meio]
        lDir = notas[meio:]

        mergeSort(lEsq, alunos)
        mergeSort(lDir, alunos)

        merge(notas, lEsq, lDir, alunos)


def merge(notas, lEsq, lDir, alunos):
    i = 0
    j = 0
    k = 0
    while i < len(lEsq) and j < len(lDir):
        if anterior(infoAluno(lEsq[i], alunos), infoAluno(lDir[j], alunos)):  # critérios de ordenação
            notas[k] = lEsq[i]
            i += 1
        else:
            notas[k] = lDir[j]
            j += 1
        k += 1

    while i < len(lEsq):
        notas[k] = lEsq[i]
        i += 1
        k += 1

    while j < len(lDir):
        notas[k] = lDir[j]
        j += 1
        k += 1


def main():
    if not os.path.isfile("entrada.bin"):
        print("O arquivo 'entrada.bin' não existe.")
    else:
        with open("entrada.bin", "rb") as arq:
            alunos = pickle.load(arq)  # dicionário {idAluno: 'nomeAluno'}
            notas = pickle.load(arq)  # lista de tuplas [(idAluno, nota1, nota2, nota3, nota4, tempoexecseg)]
        mergeSort(notas, alunos)

        for i in range(1, len(notas)+1):  # i conta as posições
            tupla = notas[i-1]

            matricula = tupla[0]
            total = tupla[1] + tupla[2] + tupla[3] + tupla[4]
            tempo = tupla[5]

            if i == 5:
                quinto = (matricula, total, tupla[5])
            if (i <= 5) or (total == quinto[1] and tempo == quinto[2]):  # se empatados com o 5º lugar, dê bônus msm assim
                total += 2

            print("%s %i" % (alunos[matricula], total))


if __name__ == "__main__":
    main()
