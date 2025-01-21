from api.src.dao.base import BaseDAO
from api.src.db.models import Words


class WordsDAO(BaseDAO):
    model = Words
