from api.src.controllers.base import BaseRouter
from api.src.dao.words import WordsDAO
from api.src.schemas.words import CreateWord, DisplayWord, SearchWord, UpdateWord

router = BaseRouter(
    entity_name="Words",
    entity_dao=WordsDAO,
    create_entity=CreateWord,
    update_entity=UpdateWord,
    display_entity=DisplayWord,
    search_entity=SearchWord,
    prefix="/words",
    tags=["words"],
)
