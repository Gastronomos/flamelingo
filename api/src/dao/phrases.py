from api.src.dao.base import BaseDAO
from api.src.db.models import Phrases


class PhrasesDAO(BaseDAO):
    model = Phrases
