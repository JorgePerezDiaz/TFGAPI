from db import get_db
from fastapi import APIRouter, HTTPException, status, Body
import APIPruebas
router = APIRouter()


@router.get("/productos")
def get_productos(producto_type = None):
    if producto_type:
        return get_db().get_productos_by_marca(producto_type)
    else:
        return get_db().list_productos()

@router.get("/productos/{producto_id}")
def get_a_productos(producto_id):
    if pro_id := get_db().get_productos_by_id(producto_id):
        return pro_id
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Producto con ID {producto_id} no existe")
        
@router.delete("/productos/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_productos(producto_id):
    try:
        get_db().delete_productos(producto_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se pudo borrar al producto con ID {producto_id}")
    
@router.post("/productos", status_code=status.HTTP_201_CREATED)
def create_producto(producto = Body()):
    print(producto)
    try:
        return get_db().insert_productos(producto.get("nombre"), producto.get("marca"), producto.get("precio"), producto.get("stock"))
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"No se pudo guardar el producto {producto}")
    
@router.put("/productos/{producto_id}")
def update_jugador(producto_id, producto = Body()):
    try:
        print(producto)
        return get_db().actualiza_productos(producto.get("nombre"), producto.get("marca"), producto.get("precio"), producto.get("stock"), producto_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se pudo updatear {producto}")