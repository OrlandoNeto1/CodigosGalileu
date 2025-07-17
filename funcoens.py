import random

#criando uma função sem parametro e sem retorno

def seja_bemvindo ():
    print ('Seja muito bem-vindo ao Galileu!')

#chamando a DEF seja bem vindo

seja_bemvindo()

#função sem parametro mas com retorno

def aleatorio_11_33 ():
    return random.randint(11, 33)

print(aleatorio_11_33())

#criando uma função com parametro e com retorno

def conta_maluca (a, b):
    resultado = (a*b) + (a**b) 
    return print (resultado)

conta_maluca(2, 5)

#criando uma função sem parametro e com retorno

def bem_vindo_aluno(nome_aluno):
    print (f'Bem vindo {nome_aluno}')

bem_vindo_aluno('Irlando')

cupom = 'GALILEUTECH'

def desconto():
    cupom1 = input("Digite o cupom:  ")
    if cupom1 == cupom:
        resultado = 1200 * (1-0.1)
        print(resultado)
    else:
        print('Este cupom não esta disponivel')
    
desconto()