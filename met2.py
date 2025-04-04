#   CRIAR METODO QUE SOMA 2 NUM.

primeiro_numero = float(input ("Digite o primeiro numero:  "))
segundo_numero = float(input("Digite o segundo numero:  "))


def somar (a,b):
    soma = a +  b #bloco de codigo
    return soma 

print(somar(primeiro_numero, segundo_numero))