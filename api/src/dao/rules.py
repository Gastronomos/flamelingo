from api.src.dao.base import BaseDAO
from api.src.db.models import Rules


class RulesDAO(BaseDAO):
    model = Rules
