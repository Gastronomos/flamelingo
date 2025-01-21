from api.src.controllers.base import BaseRouter
from api.src.dao.levels import LevelsDAO
from api.src.schemas.levels import CreateLevel, DisplayLevel, SearchLevel, UpdateLevel

router = BaseRouter(
    entity_name="Level",
    entity_dao=LevelsDAO,
    create_entity=CreateLevel,
    update_entity=UpdateLevel,
    display_entity=DisplayLevel,
    search_entity=SearchLevel,
    prefix="/levels",
    tags=["levels"],
)
