# Importa la clase FastAPI y la excepción HTTPException desde el módulo fastapi.
from fastapi import FastAPI, HTTPException

# Crea una instancia de la clase FastAPI.
app = FastAPI()

# Define una ruta para el endpoint "/" que responde con un mensaje de bienvenida.
@app.get("/")
def raiz():
    return {"message": "Bienvenido a la API de operaciones matemáticas."}

# Define una ruta para el endpoint "/sumar" que realiza la operación de suma.
@app.get("/sumar")
def sumar(a: float, b: float):
    # Realiza la suma de los números proporcionados en los parámetros de la solicitud.
    resultado = a + b
    # Retorna un diccionario con información sobre la operación y el resultado.
    return {"operacion": "suma", "resultado": resultado}

# Define una ruta para el endpoint "/restar" que realiza la operación de resta.
@app.get("/restar")
def restar(a: float, b: float):
    # Realiza la resta de los números proporcionados en los parámetros de la solicitud.
    resultado = a - b
    # Retorna un diccionario con información sobre la operación y el resultado.
    return {"operacion": "resta", "resultado": resultado}

# Define una ruta para el endpoint "/multiplicar" que realiza la operación de multiplicación.
@app.get("/multiplicar")
def multiplicar(a: float, b: float):
    # Realiza la multiplicación de los números proporcionados en los parámetros de la solicitud.
    resultado = a * b
    # Retorna un diccionario con información sobre la operación y el resultado.
    return {"operacion": "multiplicacion", "resultado": resultado}

# Define una ruta para el endpoint "/dividir" que realiza la operación de división.
@app.get("/dividir")
def dividir(a: float, b: float):
    # Verifica si el divisor (b) es cero.
    if b == 0:
        # Si es cero, lanza una excepción HTTP con un código de estado 400 y un mensaje de detalle.
        raise HTTPException(status_code=400, detail="No se puede dividir por cero.")
    
    # Realiza la división de los números proporcionados en los parámetros de la solicitud.
    resultado = a / b
    # Retorna un diccionario con información sobre la operación y el resultado.
    return {"operacion": "division", "resultado": resultado}
