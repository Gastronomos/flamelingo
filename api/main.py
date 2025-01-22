from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette_admin.contrib.sqla import Admin

from api.src.admin.auth import UsernameAndPasswordProvider
from api.src.admin.views import (
    FlowerView,
    LevelAdmin,
    OAuthAccountView,
    PhraseAdmin,
    RuleAdmin,
    TopicAdmin,
    UserView,
    WordAdmin,
)
from api.src.controllers.levels import router as level_router
from api.src.controllers.phrases import router as phrase_router
from api.src.controllers.rules import router as rule_router
from api.src.controllers.topics import router as topic_router
from api.src.controllers.users import router as user_router
from api.src.controllers.words import router as word_router
from api.src.db.config import async_engine
from api.src.db.models import Levels, OAuthAccount, Phrases, Rules, Topics, Users, Words

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

admin = Admin(
    async_engine,
    auth_provider=UsernameAndPasswordProvider(),
    templates_dir="api/templates/starlette_admin",
)

admin.add_view(UserView(Users))
admin.add_view(OAuthAccountView(OAuthAccount))
admin.add_view(TopicAdmin(Topics))
admin.add_view(LevelAdmin(Levels))
admin.add_view(PhraseAdmin(Phrases))
admin.add_view(RuleAdmin(Rules))
admin.add_view(WordAdmin(Words))
admin.add_view(FlowerView(label="Flower", icon="fa-solid fa-seedling", path="/flower", template_path="flower.html"))

admin.mount_to(app)
