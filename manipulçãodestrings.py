#toda string é indexavel,ou seja possui um mapa de posição
#python ele começa sempre do 0
#indices em python sao representados por colchetes


nome = "Orlando" 
print(nome[2])

nome_zuado = "sSDaisdhaisudaisdnasiduasuidhadoaiejasduiaosidjeaohfaiusioapowdoiasdiuahféshsoauhehaiushdauihisudhiuasuygdah"
print(nome_zuado[-1])
#-1 igual a pegar X posição

numero_grande= 8.79841984412747478427842178474724828724721872794272187124272176523725427945768217
print(f"{numero_grande:.2f}")

#separador e milhar
conta_bancaria=2000000
print(f"{conta_bancaria:,}") 

#frase base para dominar varios metodos de manu=ipulação de string

frase = input("Escolha uma frase:  ")
frutas = "Maçã, Morango, Uva"
lista_palavras = ["Álvaro","mora", "no", "parque" ,"do", "lago"]
frase_zuada = "            OrlAnDo TEM Um CAChoRro CHamaDo TObias, ElE É uM SHITZU"
#METODO "X()"DA BIBLIOTECA PADRÃO DE STRINGS DO PYTHON

print(frase.capitalize())#coloca a primeira letra da frase em maiusculo
print (frase.title())# coloca a primeira letra de cada palavra em maiusculo
print(frase.upper())# coloca toda frase em maiuscula
print(len(frase))#conta a qtd de caracteres de uma frase
print(frase.lower())#coloca toda frase em letra minuscula
print(frase.center(50,'_'))#centraliza uma palavra repitindo os caracteres informados, SOMENTE COM UMA PALAVRA
print(frase.find("ontem!"))#retorna a posição da primeira letra encontrada
print(frase.replace('alvaro', 'orlando'))#substitui uma palavra por outra especificada
print(frase.startswith("a"))#verifica se a primeira letra da frase é a letra especificada
print(frase.endswith("é"))#verifica primeira letra da frase é a letra especificicada
print(frutas.split(', '))#vai pegar a 'frutas' e retornar uma lista com cada tipo de fruta separada por virgula
print(" ".join(lista_palavras))#alvaro mora no parque do lago
frase_formatada = frase_zuada.title().strip().replace("Shitzu", "Alemão")
print(frase_formatada)