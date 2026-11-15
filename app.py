from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from consulta import consultar_clima

app = FastAPI()
modelos = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request, endereco: str = ""):
    resultado = None
    erro = None

    if endereco != "":
        resultado = consultar_clima(endereco)
        if resultado is None:
            erro = "Endereço não encontrado"

    return modelos.TemplateResponse(
        request=request,
        name="index.html",
        context={"endereco": endereco, "resultado": resultado, "erro": erro},
        )    

