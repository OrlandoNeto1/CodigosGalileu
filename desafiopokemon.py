import random

pokemons = {
    'Charmander': {'Ataque': 'Bola de Fogo', 'Dano': 35},
    'Squirtle': {'Ataque': 'Jato de água', 'Dano': 32},
    'Bulbassauro': {'Ataque': 'Chicote de planta', 'Dano': 30},
}

print ("Charmander': {'Ataque': 'Bola de Fogo', 'Dano': 35")
print("Squirtle': {'Ataque': 'Jato de água', 'Dano': 32")
print("Bulbassauro': {'Ataque': 'Chicote de planta', 'Dano': 30")
print("_"*40)
escolha1 = input("Escolha seu pokemon:  ")

def pokemon1 (jogador1):
    escolha1 = input("Escolha seu pokemon:  ")
    if pokemon1 in pokemons:
        print("Escolha do Jogador 1 Feita com sucesso!")

def pokemon2 (jogdor2):
    escolha2 = input("Escolha seu pokemon:  ")
    if pokemon2 in pokemons:
        print("Escolha do Jogador 2 Feita com sucesso!")

pokemon1()
pokemon2()