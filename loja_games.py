loja_games_minecraft = {

'Minecraft' : {'preço' : 59.90, 'estoque': 5},
'Fifa23' :    {'preço' : 199.90, 'estoque' :3 },
'God Of War': {'preço': 149.90, 'estoque' :4 }

}

print(loja_games_minecraft['Minecraft']['estoque'])

for jogo, info in loja_games_minecraft.items:

    print(f'Jogo : {jogo}')
    print(f'Preço : {info['preço']}')
    print(f'Preço{info['estoque']}')
    print('-'*40)