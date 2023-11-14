from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def raiz():
    return {"message": "Bienvenido a la API de operaciones matemáticas. Consulta la documentación en /docs."}

@app.get("/sumar")
def sumar(a: float, b: float):
    resultado = a + b
    return {"operacion": "suma", "resultado": resultado}

@app.get("/restar")
def restar(a: float, b: float):
    resultado = a - b
    return {"operacion": "resta", "resultado": resultado}

@app.get("/multiplicar")
def multiplicar(a: float, b: float):
    resultado = a * b
    return {"operacion": "multiplicacion", "resultado": resultado}

@app.get("/dividir")
def dividir(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir por cero.")
    
    resultado = a / b
    return {"operacion": "division", "resultado": resultado}
