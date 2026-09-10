from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status" : "OK"}
@app.get("/saudável")
def checando_saude():
    return {"status" : "saudável"}
