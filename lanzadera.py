import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from consultas import router

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Permite solicitudes de cualquier origen
    allow_methods=['*'],  # Métodos HTTP permitidos
    allow_headers=['*']   # Encabezados permitidos
)

@app.get("/")
def get_root():
    return "Hello World"

@app.get("/health")
def health_check():
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
