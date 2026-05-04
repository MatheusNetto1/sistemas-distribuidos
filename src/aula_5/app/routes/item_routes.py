# app/routes/item_routes.py
from fastapi import APIRouter, HTTPException
from app.schemas.item import ItemCreate
from app.services.item_service import ItemService

router = APIRouter()
service = ItemService()

@router.get("/items")
async def listar():
    return await service.listar()

@router.post("/items")
async def criar(item: ItemCreate):
    return await service.criar(item)

@router.get("/items/{item_id}")
async def buscar(item_id: int):
    item = await service.buscar_por_id(item_id)
    if not item:
        raise HTTPException(404, "Item não encontrado")
    return item

@router.put("/items/{item_id}")
async def atualizar(item_id: int, item: ItemCreate):
    atualizado = await service.atualizar(item_id, item)
    if not atualizado:
        raise HTTPException(404, "Item não encontrado")
    return atualizado

@router.delete("/items/{item_id}")
async def deletar(item_id: int):
    if not await service.deletar(item_id):
        raise HTTPException(404, "Item não encontrado")
    return {"mensagem": "Deletado com sucesso"}