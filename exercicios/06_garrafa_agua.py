# %%

agua = input("Vende-se água mineral natural ou com gás. Qual a sua escolha? ")

print(agua)

if agua == "Mineral":
    print("O valor é R$ 1,50")

elif agua == "Com gás":
    print("O valor é R$ 2,50")

else:
    print("Opção inválida.")


# %%

texto = """
Escolha a sua água para comprar:
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)

if opcao == "1":
    print("O valor é R$ 1,50")

elif opcao == "2":
    print("O valor é R$ 2,50")

else:
    print("Opção inválida.")    
