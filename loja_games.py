loja_games = {

'Minecraft' : {'preço' : 59.90, 'estoque': 5},
'Fifa23' :    {'preço' : 199.90, 'estoque' :3 },
'God Of War': {'preço': 149.90, 'estoque' :4 }

}

carrinho_de_compras = {}

for jogo, info in loja_games.items():

    print(f'Jogo : {jogo}')
    print(f'Preço : {info['preço']}')
    print(f'Estoque : {info['estoque']}')
    print('-'*40)

escolha_usuario = input ("Qual jogo você deseja:  ").strip().title()

if escolha_usuario in loja_games:
    escolha_qtdade = int(input ("Quantas unidades você deseja?:  "))
    if escolha_qtdade <= loja_games[escolha_usuario]['estoque']:
        loja_games[escolha_usuario]['estoque']-= escolha_qtdade
        