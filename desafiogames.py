#Sistema de cadastro de jogadores

#usuário coloca o numero de jogadores a ser cadastrado

qtdadecadastro = int(input("Digite a quantidade de cadastros:  "))

for c in range(qtdadecadastro):
    nomecplt = input ("Qual seu nome? (*completo)")
    idade = int(input("qual sua idade?  "))
    nome = input("Qual seu nickname?  ")
    jogopcp = input("Qual seu jogo principal:  ")
    streamer = input("Você é streamer? (*S ou N) ")
    nomecompletoform = nomecplt.title()
    jogoformat = jogopcp.capitalize()
    nicknameformat = nome.strip().lower().replace(" ", "_")

    print(f"Cadastro #{c+ 1}".center(30, '_'))
    print(f"Nome:{nomecompletoform}")
    print(f"Jogo principal:{jogoformat}")
    print(f"Nickname:{nicknameformat}")
    print(f"Idade:{idade}")

    if streamer == 'S':
        print("O participante é streamer!")

    elif streamer == 'N':
        print("O participante não é streamer")
    
    else:
        print("Não entendi; desculpe!")