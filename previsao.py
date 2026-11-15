import httpx

def buscar_previsao(latitude, longitude):
    pedido = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
        "daily": "temperature_2m_max,temperature_2m_min",
        "temperature_unit": "fahrenheit",
        "timezone": "auto",
        "forecast_days": 5,
    }

    resposta = httpx.get("https://api.open-meteo.com/v1/forecast", params=pedido)
    dados = resposta.json()

    dias = []
    for i in range(5):
        dias.append(
            {
                "data": dados["daily"]["time"][i],
                "maxima": dados["daily"]["temperature_2m_max"][i],
                "minima": dados["daily"]["temperature_2m_min"][i],
            }
        )

    return {
        "temperatura_atual": dados["current"]["temperature_2m"],
        "dias": dias,
    }