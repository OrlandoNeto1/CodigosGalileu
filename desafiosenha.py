senharegistrada = input ("Digite a senha:  ")
senhatentativa = input("Confirme a senha:  ")

def confirmação (senharegistrada):
    if senharegistrada == senhatentativa:
        print ("Tudo certo!")
    else:
        print ("Tente novamente")


confirmação(senharegistrada)