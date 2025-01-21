from api.src.dao.base import BaseDAO
from api.src.db.models import Users


class UsersDAO(BaseDAO):
    model = Users
