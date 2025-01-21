from api.src.dao.base import BaseDAO
from api.src.db.models import Topics


class TopicsDAO(BaseDAO):
    model = Topics
