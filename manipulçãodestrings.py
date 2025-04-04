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
frase = "Eu hackiei o Bing"

#METODO CAPITALIZE()DA BIBLIOTECA PADRÃO DE STRINGS DO PYTHON
print(frase.capitalize())#coloca a primeira letra da frase em maiusculo
print (frase.title())# coloca a primeira letra de cada palavra em maiusculo