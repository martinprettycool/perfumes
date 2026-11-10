from fastapi import Fastapi

app = Fastapi()

@app.get("/perfumes")
def ver_perfumes():
    return {"hola": "mundo"}