# main.py - il server del ping-pong, con la sua pagina web
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# 1. Creiamo l'applicazione e rendiamo raggiungibile la cartella static
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# 2. I dati che la rotta POST /gioca riceve: la parola del colpo
class Colpo(BaseModel):
    parola: str


# 3. La pagina principale: il file index.html
@app.get("/")
def home():
    return FileResponse("static/index.html")


# 4. Ping: nessun dato, la risposta è sempre pong
@app.get("/ping")
def ping():
    return {"risposta": "pong"}


# 5. Il colpo con GET: la parola arriva nell'indirizzo
@app.get("/gioca")
def gioca(parola: str):
    if parola.strip().lower() == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}


# 6. Il colpo con POST: la parola arriva in JSON, nel corpo della richiesta
@app.post("/gioca")
def gioca_post(colpo: Colpo):
    if colpo.parola.strip().lower() == "ping":
        return {"risposta": "pong"}
    return {"risposta": "Non ho capito: scrivi ping"}