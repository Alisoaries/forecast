from localizacao import buscar_coordenadas
from previsao import buscar_previsao
from cache import buscar_no_cache, guardado_no_cache

def consultar_clima(endereco):
    local = buscar_coordenadas(endereco)
    if local is None:
        return None

    chave = local["cep"]
    if chave is None:
        chave = str(local["latitude"]) + "," + str(local["longitude"])

    clima = buscar_no_cache(chave)
    do_cache = clima is not None

    if not do_cache:
        clima = buscar_previsao(local["latitude"], local["longitude"])
        guardado_no_cache(chave, clima)

    return {"local": local, "clima": clima, "do_cache": do_cache}    
