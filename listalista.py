lista_clientes =  [
    ['Álvaro' , 'alvaros.sampaio@galileunegocio.com.br', 32],
    ['Felipe' , 'felipe.nasciben@galileunegocios.com.br', 41],
    ['Matheus', 'matheus.biazoto@galileunegocios.com.br', 29]
]
print (lista_clientes[1][2])
print (lista_clientes[2][1])

lista_frutas = ['morango', 'banana', 'melancia']
#metodo .append, ele adiciona um elemento no final de uma lista
lista_frutas.append('Caju')
lista_frutas.append('banana')
print (lista_frutas)

#metodo .insert(posição e elemento)
lista_frutas.insert(2, "Kiwi")
print (lista_frutas)



#metodo .remove(X), remove a primeira ocorrencia de um elemento
lista_frutas.remove('banana')
print (lista_frutas)

lista_numeros = [30,37,13,48,2,11]
lista_numeros.sort(reverse=True)#reverse=False, ordenado menor para o maior
print (lista_numeros)
#metodo .count(elemento), retorna o numero de vezes que um elemento esta em uma lista
lista_frutas.append('banana')
print(lista_frutas.count('banana'))#2

#metodo .len(lista) retorna o tam da lista
print(len(lista_frutas))

#metodo .index(ELEMENTO), retornar a posição do elemento especificado da primeira vez espcificado
print (lista_frutas)
print(lista_frutas.index('Caju'))
 
notas = [  
    ["Ana", [8 ,7 ,9]],
    ["Carlos", [5,6,7]],
    ["João", [10,9,8]]
]

for a in notas :
    media = sum(a[1])/ len(a[1])
    print (f"A media do aluno {a[0]} é de: {media}")
    