from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://6434848e676ada40403cd30b5ee23164@o4512062442766336.ingest.us.sentry.io/4512062460723200",
    send_default_pii=True
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"status" : "OK"}
@app.get("/saudável")
def checando_saude():
    return {"status" : "saudável"}

#Rota de teste utilizada para validar o monitoramento do Sentry / Desativada em produção
#@app.get("/erro")
#def forcar_erro():
#    return 1/0
