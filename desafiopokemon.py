pokemons = {
    'Charmander': {'Ataque': 'Bola de Fogo', 'Dano': 35},
    'Squirtle': {'Ataque': 'Jato de água', 'Dano': 32},
    'Bulbassauro': {'Ataque': 'Chicote de planta', 'Dano': 30},
}


def escolha_pokemon ():
    print ("Faça Sua escolha: ".center(40 , '-'))
    print ("1 = Charmander \n2 = Squirtle  \n3 = Bulbassauro")
    escolha = int(input("Selecione 1, 2 ou 3:  "))
    if escolha == 1:
        escolha = 'Chamander'
    elif escolha == 2:
        escolha = 'Squirtle'
    elif escolha == 3:
        escolha = 'Bulbassauro'
    else:
        print("Desculpe não entendi! Digite 1, 2 ou 3")
    return escolha


jogador1 = escolha_pokemon()
jogador2 = escolha_pokemon()

print(jogador1)
print(jogador2)