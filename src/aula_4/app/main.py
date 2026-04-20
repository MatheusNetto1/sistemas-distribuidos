from fastapi import FastAPI

from app.routes.item_routes import router as item_router
from app.middlewares.logging import log_requests
from app.middlewares.custom_header import add_custom_header

app = FastAPI(
    title="Middleware CRUD API",
    description="API para estudo de middleware e operações CRUD com FastAPI",
    version="1.0.0"
)

# ==============================
# Registro dos Middlewares
# ==============================
app.middleware("http")(log_requests)
app.middleware("http")(add_custom_header)

# ==============================
# Rotas
# ==============================
app.include_router(item_router)

# ==============================
# Health Check
# ==============================
@app.get("/")
def root():
    return {"mensagem": "API funcionando 🚀"}