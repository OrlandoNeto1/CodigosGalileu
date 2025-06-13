pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]

pedidos_entregues = []
pedidos_valores = []
soma_cancelado = 0
escolha_categoria = []


for n in pedidos:
    if n[3] == 'Entregue':
        print(f"Pedido: {n[0]} {n[3]}")
        pedidos_valores.append(n[2])
        pedidos_entregues.append(n[0])
    if n[1] == 'Vestuário' and n[3] == 'Cancelado':
        soma_cancelado += 1

print(f"Valor Total: {sum(pedidos_valores)}")
print(f"Cancelados da categoria Vestuário: {soma_cancelado}")
print(f"Últimos 3 pedidos entregues: {pedidos_entregues[-3:]}")

escolha_categoria = input ("Escolha uma categoria:  ")

for n in pedidos:
    if escolha_categoria == n[1]:
        print (f"Itens desta categoria: {n[0]}")

