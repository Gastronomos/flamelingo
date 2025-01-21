from api.src.dao.base import BaseDAO
from api.src.db.models import Levels


class LevelsDAO(BaseDAO):
    model = Levels
