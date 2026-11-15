from consulta import consultar_clima

endereco = "Rua Airão 7, São Paulo"

for tentativa in range(2):
    print("---consulta", tentativa +1)
    resultado = consultar_clima(endereco)

    if resultado is None:
        print("Endereço não encontrado")
    else:
        print("Local", resultado["local"]["nome"])
        print("Temperatura agora:", resultado["clima"]["temperatura_atual"], "C")
        if resultado["do_cache"]:
            print("(Resultado veio do CACHE)")
        else:
            print("(Resultado veio da API)")    
    