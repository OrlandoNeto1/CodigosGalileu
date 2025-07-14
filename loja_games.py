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
while True: #roda infinito até digitar sair
     
    escolha_usuario = input ("Qual jogo você deseja:  (Caso queira encerrar digite 'Sair'):      ").strip().title()
   
    if escolha_usuario == 'Sair':
        break 
    if escolha_usuario in loja_games:
        escolha_qtdade = int(input ("Quantas unidades você deseja?:  "))
        if escolha_qtdade <= loja_games[escolha_usuario]['estoque']:
            loja_games[escolha_usuario]['estoque']-= escolha_qtdade
            if escolha_usuario in carrinho_de_compras:
                carrinho_de_compras += escolha_qtdade
            else:
                carrinho_de_compras.setdefault(escolha_usuario, escolha_qtdade)
        else:
            print('Não temos esta quantidade, desculpe!')
    else:
        print('Não temos esse jogo disponivel, desculpe!')


total = 0
for jogo , qtd in carrinho_de_compras.items():
    preço = loja_games[jogo]["preço"]
    total += preço * qtd

print (carrinho_de_compras)


#print(carrinho_de_compras)
#print('-'*40)
#print(loja_games[escolha_usuario]['estoque'])