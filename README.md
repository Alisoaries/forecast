# Previsão do tempo por endereço

Aplicação web simples que recebe um endereço dos Estados Unidos e mostra a previsão do tempo.

## O que ela faz

- Recebe um **endereço** em um formulário.
- Descobre as coordenadas e o **zip code** do endereço.
- Busca a temperatura atual e a previsão de 5 dias (máxima e mínima).
- Guarda o resultado em **cache por 30 minutos**, usando o zip code como chave.
- Mostra um **aviso na tela** quando o resultado veio do cache.

## Como funciona

1. O endereço digitado é enviado ao serviço **Nominatim** (OpenStreetMap), que devolve latitude, longitude e zip code.
2. Se já existe uma previsão guardada para esse zip code há menos de 30 minutos, ela é reaproveitada.
3. Senão, as coordenadas são enviadas à API **Open-Meteo**, e o resultado é guardado no cache.

Nenhuma das duas APIs exige chave de acesso.

## Estrutura do projeto

| Arquivo                | Função                                      |
| ---------------------- | ------------------------------------------- |
| `app.py`               | Servidor web (FastAPI) e rota da página     |
| `templates/index.html` | Página com o formulário e o resultado       |
| `consulta.py`          | Junta localização, cache e previsão         |
| `localizacao.py`       | Converte endereço em coordenadas e zip code |
| `previsao.py`          | Busca a previsão do tempo                   |
| `cache.py`             | Cache em memória com validade de 30 minutos |

## Como executar

Requer Python 3.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Depois, abra `http://127.0.0.1:8000` no navegador.

Exemplos de entrada:

- `1600 Pennsylvania Avenue NW, Washington, DC 20500`
- `350 5th Ave, New York, NY 10118`
- `90210`

## Limitações conhecidas

- O cache fica na memória: ao reiniciar o servidor, ele é perdido.
- Endereços incompletos podem ser interpretados como outro lugar. Por isso a página mostra o endereço que foi encontrado.
- A busca de endereços usa um serviço gratuito, sujeito a limites de uso.

## Como conferir o cache

1. Busque `90210` e veja a mensagem **Resultado consultado agora na API**.
2. Busque `90210` de novo, em até 30 minutos.
3. A mensagem deve mudar para **Resultado veio do CACHE**.