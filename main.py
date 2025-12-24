from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API de Clima", version="1.0.0")

# Datos de ejemplo de ciudades y clima
datos_clima = {
    "lima": {
        "ciudad": "Lima",
        "temperatura": 28,
        "descripcion": "Soleado",
        "humedad": 65,
        "velocidad_viento": 15
    },
    "arequipa": {
        "ciudad": "Arequipa",
        "temperatura": 22,
        "descripcion": "Nublado",
        "humedad": 45,
        "velocidad_viento": 20
    },
    "cusco": {
        "ciudad": "Cusco",
        "temperatura": 15,
        "descripcion": "Lluvia",
        "humedad": 80,
        "velocidad_viento": 10
    },
    "tacna": {
        "ciudad": "Tacna",
        "temperatura": 30,
        "descripcion": "Muy soleado",
        "humedad": 35,
        "velocidad_viento": 25
    }
}

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de Clima", "ciudades_disponibles": list(datos_clima.keys())}

@app.get("/clima/{ciudad}")
def obtener_clima(ciudad: str):
    """Obtiene el clima de una ciudad"""
    ciudad_lower = ciudad.lower()
    if ciudad_lower in datos_clima:
        return datos_clima[ciudad_lower]
    return {"error": f"Ciudad '{ciudad}' no encontrada. Ciudades disponibles: {list(datos_clima.keys())}"}

@app.get("/clima")
def obtener_clima_query(ciudad: Optional[str] = None):
    """Obtiene el clima por query parameter"""
    if not ciudad:
        return {"error": "Por favor proporciona una ciudad"}
    
    ciudad_lower = ciudad.lower()
    if ciudad_lower in datos_clima:
        return datos_clima[ciudad_lower]
    return {"error": f"Ciudad '{ciudad}' no encontrada"}

@app.get("/ciudades")
def listar_ciudades():
    """Lista todas las ciudades disponibles"""
    return {"ciudades": list(datos_clima.keys()), "total": len(datos_clima)}