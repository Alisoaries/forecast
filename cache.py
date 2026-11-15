import time

TEMPO_DE_VIDA = 30 * 60

guardados = {}

def guardado_no_cache(chave, valor):
    guardados[chave] = {"valor": valor, "momento": time.time()}

def buscar_no_cache(chave):
    item = guardados.get(chave)

    if item is None:
        return None

    idade = time.time() - item["momento"]
    if idade > TEMPO_DE_VIDA:
        del guardados[chave]
        return None

    return item["valor"]

