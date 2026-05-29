def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        if chute == item:
            print(f"✅ Encontrado! O número {item} está na posição {meio}")
            return meio
        if chute > item:
            print(f"📉 Chute alto: tentei {chute}, mas o número é menor")
            alto = meio - 1
        else:
            print(f"📈 Chute baixo: tentei {chute}, mas o número é maior")
            baixo = meio + 1

    print(f"❌ O número {item} não está na lista")
    return None


minha_lista = [1, 3, 5, 7, 9]

print("--- Buscando 7 ---")
pesquisa_binaria(minha_lista, 7)

print("\n--- Buscando 1 ---")
pesquisa_binaria(minha_lista, 1)

print("\n--- Buscando -1 ---")
pesquisa_binaria(minha_lista, -1)