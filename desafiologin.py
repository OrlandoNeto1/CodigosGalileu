#Escreva um programa que peça e valide um login e uma senha

login = input ("Digite um nome de usuario:  ")
senha = input ("DIgite uma senha:  ")
usuario = input ("Digite seu usuario:  ")
tentativasenha = input ("Digite sua senha:  ")



while tentativasenha != senha and usuario != login:
    print("Você errou! Digite novamente:  ")
    usuario= input("Digite seu usuario:  ")
    tentativasenha= input ("Digite sua senha:  ")
    

if tentativasenha == senha and usuario == login:
    print("Entrou com sucesso!")