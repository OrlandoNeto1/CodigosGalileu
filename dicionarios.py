#Estrutura de dados organizada em pares (chaves e valor)
#São mutaveis, indexaveis, não pode ter o mesmo nome 2 vezes, aceita qualquer tipo de dado, é representado por {}, é iteravel



skin_raras_fortinite = {

    'balãozinho' : 'Honor Guard' ,
    'embananinho': 'Galaxy',
    'rato_opressor' : 'Black Knite'

}

print (skin_raras_fortinite.get('balãozinho'))#
print (skin_raras_fortinite.keys())#retorna todas as chaves de um dicionario
print (skin_raras_fortinite.values())#retorna os valores
skin_raras_fortinite.setdefault('medoinha' , 'Ragnarok')#add chave e retorna o valor
print (skin_raras_fortinite.items())#retorna tudo!
skin_raras_fortinite.clear()#remove todas as chaves e valores do dicionario
print(skin_raras_fortinite.items())