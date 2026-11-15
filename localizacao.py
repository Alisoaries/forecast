import httpx

def buscar_coordenadas(endereco):
    pedido = {
        "q": endereco,
        "format": "json",
        "addressdetails": 1,
        "limit": 1,
        "countrycodes": "us",
    }

    cabecalhos = {"User-Agent": "estudo-previsao-clima"}

    resposta = httpx.get(
        "https://nominatim.openstreetmap.org/search",
        params=pedido,
        headers=cabecalhos,
    )

    resultados = resposta.json()

    if len(resultados) == 0:
        return None

    lugar = resultados[0]
    return {
        "nome": lugar["display_name"],
        "latitude": float(lugar["lat"]),
        "longitude": float(lugar["lon"]),
        "cep": lugar["address"].get("postcode"),
    }