from fastapi import FastAPI
from app.api import router
from app.models import Base
from app.db import engine

Base.metadata.create_all(bind=engine)  # ← Membuat DB & tabel

app = FastAPI()

app.include_router(router)
