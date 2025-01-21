from api.src.controllers.base import BaseRouter
from api.src.dao.phrases import PhrasesDAO
from api.src.schemas.phrases import CreatePhrase, DisplayPhrase, SearchPhrase, UpdatePhrase

router = BaseRouter(
    entity_name="Phrase",
    entity_dao=PhrasesDAO,
    create_entity=CreatePhrase,
    update_entity=UpdatePhrase,
    display_entity=DisplayPhrase,
    search_entity=SearchPhrase,
    prefix="/phrases",
    tags=["phrases"],
)
