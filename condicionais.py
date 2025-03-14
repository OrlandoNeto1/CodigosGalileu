idade_orlando = int(input("Digite sua idade:  "))
carteira = input("Você tem cateira de motorista?: (Responda 'S' para sim e 'N' para não) ")


#VOU DETALHAR UMA CONDICIONAL PARA VERIFICAR SE A IDADE É MAIOR DE 18 ANOS

if idade_orlando >= 18 and carteira == 'S':
     print("Você pode dirigir!")

elif carteira != 'S' or 'N':
    print("Não entendi! Digite 'S' ou 'N'!:  ")


else:
     print("Você não pode dirigir")