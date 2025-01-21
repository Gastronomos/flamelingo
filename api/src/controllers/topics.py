from api.src.controllers.base import BaseRouter
from api.src.dao.topics import TopicsDAO
from api.src.schemas.topics import CreateTopic, DisplayTopic, SearchTopic, UpdateTopic

router = BaseRouter(
    entity_name="Topic",
    entity_dao=TopicsDAO,
    create_entity=CreateTopic,
    update_entity=UpdateTopic,
    display_entity=DisplayTopic,
    search_entity=SearchTopic,
    prefix="/topics",
    tags=["topics"],
)
