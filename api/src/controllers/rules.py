from api.src.controllers.base import BaseRouter
from api.src.dao.rules import RulesDAO
from api.src.schemas.rules import CreateRule, DisplayRule, SearchRule, UpdateRule

router = BaseRouter(
    entity_name="Rule",
    entity_dao=RulesDAO,
    create_entity=CreateRule,
    update_entity=UpdateRule,
    display_entity=DisplayRule,
    search_entity=SearchRule,
    prefix="/rules",
    tags=["rules"],
)
