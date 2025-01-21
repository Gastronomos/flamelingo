from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.src.controllers.users import router as user_router

app = FastAPI()

app.include_router(user_router)

app.mount("/files", StaticFiles(directory="files"), name="files")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
