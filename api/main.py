from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.src.controllers.levels import router as level_router
from api.src.controllers.phrases import router as phrase_router
from api.src.controllers.rules import router as rule_router
from api.src.controllers.topics import router as topic_router
from api.src.controllers.users import router as user_router
from api.src.controllers.words import router as word_router

app = FastAPI()

app.include_router(user_router)
app.include_router(topic_router)
app.include_router(level_router)
app.include_router(phrase_router)
app.include_router(word_router)
app.include_router(rule_router)

app.mount("/files", StaticFiles(directory="files"), name="files")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
