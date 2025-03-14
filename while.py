resposta = input("Digite 'S' para sim e 'N' para não : ")
resposta_tentativa = str(input("Digite 'S' para sim e 'N' para não : "))
#ENQUANTO A RESPOSTA FOR DIFERENTE DE s OU n QUERO QUE REPITA O INPU
while resposta != 'S' or resposta !='N':
    print("Você errou! Digite novamente!")
    resposta = input("Digite 'S' para sim e 'N' para não : ")
     
if resposta == 'S' or resposta == 'N':
    print("Resposta aceita! Obrigado!")