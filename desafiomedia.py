lista_notas = []

while True:
    nota = float(input ("Digite a nova nota: (Digite '999' para encerrar)  "))
    if nota == 999:
        break
    else:
        lista_notas.append(nota)

def calcular_media (lista_notas_recebida):
    media = sum(lista_notas) / len(lista_notas) 
    return media

print(calcular_media(lista_notas))

def avaliar_aluno(nome_aluno, n = calcular_media(lista_notas)):
    if n >= 9 and n <= 10:
        print(f'Parabens {nome_aluno}! Excelente desempenho!')
    elif n >= 7 and n <= 8.9:
        print(f'Muito bem, {nome_aluno}! Você esta indo bem')
    elif n >= 5 and n <= 6.9:
        print(f'atenção, {nome_aluno}!Você precisa se dedicar mais!')
    else:
        print("Melhore!")

def main (): 
    nome = input ("Digite seu nome:  ")
    avaliar_aluno(nome)

if __name__ == '__main__':
    main()