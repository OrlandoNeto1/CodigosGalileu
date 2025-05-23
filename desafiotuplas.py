tulpa_tupla = (
    ('Mouse LG Tech', 10),
    ('Mic Hyper X', 5),
    ('Acer Nitro 5', 3),
    ('Webcam HD', 0)
)
for i in tulpa_tupla:
    if i[1] <5:#verificando os produtos com menos de 5 unidades
       print(f'Item com menos de 5 unidades : {i[0]} ') 
contador = 0



for m in tulpa_tupla:
    if m[1] ==0:
        contador = 0
        contador += 1
print(f'Produtos esgotados: {contador}')
soma_acumulada = 0
for d in tulpa_tupla:
    soma_acumulada += d[1]
print(f'O total de itens é : {soma_acumulada}')