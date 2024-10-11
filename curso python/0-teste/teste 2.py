# produtos
pp = "pizza pequena"
pm = "pizza média"
pg = "pizza grande"

#pizza doce
pequena = "pequena"
média = "média"

# preços
p = 30.00
m = 50.00
g = 70.00
pdp = 40.00
pdm = 50.00

# sabores salgados
mg = "marguerita"
pt = "portuguesa"
cb = "calabresa"
qq = "quatro queijos"

# sabores doces
bn = "banana"
bc = "banana com chocolate"
bnv = "banana nevada"
rl = "romeu e julieta" 

produtos = input(f"{pp} R$ {p}\n{pm} R$ {m}\n{pg} R$ {g}\nEscolha o tamanho das pizzas: ")

while produtos not in ["pizza pequena", "pizza média", "pizza grande"]:
    print("Produto inválido")
    produtos = input(f"{pp} R$ {p}\n{pm} R$ {m}\n{pg} R$ {g}\nEscolha o tamanho das pizzas: ")
print(f"Você escolheu a {produtos}")

sabores = input(f"{mg}\n{pt}\n{cb}\n{bn}\nEscolha o sabor da pizza: ")

while sabores not in ["marguerita", "portuguesa", "calabresa", "quatro queijos"]:
    print("Sabor inválido")
    sabores = input(f"{mg}\n{pt}\n{cb}\n{bn}\nEscolha o sabor da pizza: ")

if produtos == "pizza pequena":
    print("A pizza escolhida foi a pequena.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = p * quantidade
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {pp}(s) de {sabores}")
    print(f"Sua compra total foi: R$ {total}")

elif produtos == "pizza média":
    print("A pizza escolhida foi a média.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = m * quantidade
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {pm}(s) de {sabores}")
    print(f"Sua compra total foi: R$ {total}")

elif produtos == "pizza grande":
    print("A pizza escolhida foi a grande.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = g * quantidade 
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {pg}(s) de {sabores}")
    print(f"Sua compra total foi: R$ {total}")

else:
    print("Tipo de pizza inválido")