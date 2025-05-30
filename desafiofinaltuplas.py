pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]

for n in pedidos:
    if n[3] == 'Entregue':
        print(f"Pedido: {n[0]} {n[3]}")
pedido = []
        
for n in pedidos:
    if n[3] == 'Entregue':
        pedido.append(n[2])

print (f"Valor Total: {sum(pedido)}")

