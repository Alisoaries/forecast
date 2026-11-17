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

    try:
        resposta = httpx.get(
            "https://nominatim.openstreetmap.org/search",
            params=pedido,
            headers=cabecalhos,
            timeout=10,
        )
        resposta.raise_for_status()
    except httpx.HTTPError:
        return None

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