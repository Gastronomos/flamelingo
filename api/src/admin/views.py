from fastapi.responses import HTMLResponse
from markupsafe import Markup
from sqladmin import BaseView, ModelView, expose

from api.src.db.models import Levels, OAuthAccount, Phrases, Rules, Topics, Users, Words
from api.src.settings import settings


class BaseModelView(ModelView):
    route = None
    list_template = "sqladmin/list_custom.html"


class UserAdmin(ModelView, model=Users):
    name_plural = "Users"
    name = "User"
    column_list = ["id", "username", "email", "is_active", "is_superuser", "is_verified", "created_at"]
    column_searchable_list = ["username", "email"]
    column_filters = ["is_active", "is_superuser", "is_verified"]
    column_sortable_list = ["username", "email", "is_active", "is_superuser", "is_verified", "created_at"]
    column_editable_list = ["is_active", "is_superuser", "is_verified"]
    column_details_exclude_list = ["hashed_password"]
    can_delete = False


class OAuthAdmin(ModelView, model=OAuthAccount):
    name_plural = "OAuth Accounts"
    name = "OAuth Account"
    column_list = ["id", "user_id"]
    column_searchable_list = ["id", "user_id"]
    column_filters = ["user_id"]
    column_sortable_list = ["id", "user_id"]
    can_delete = False
    can_edit = False


class TopicAdmin(BaseModelView, model=Topics):
    route = "topics"
    name_plural = "Topics"
    name = "Topic"
    column_list = ["id", "name", "description"]
    column_searchable_list = ["name", "description"]
    column_filters = ["name"]
    column_sortable_list = ["name"]
    column_editable_list = ["name", "description"]


class LevelAdmin(BaseModelView, model=Levels):
    route = "levels"
    name_plural = "Levels"
    name = "Level"
    column_list = ["id", "stages", "topic"]
    column_searchable_list = ["stages"]
    column_filters = ["stages"]
    column_sortable_list = ["stages"]
    column_editable_list = ["stages", "topic"]


class WordAdmin(BaseModelView, model=Words):
    route = "words"
    name_plural = "Words"
    name = "Word"
    column_list = ["id", "ru", "en", "part_of_speech", "level", "topic"]
    column_searchable_list = ["ru", "en", "part_of_speech", "level"]
    column_filters = ["ru", "en"]
    column_sortable_list = ["ru", "en"]
    column_editable_list = ["ru", "en", "part_of_speech", "level", "topic"]


class PhraseAdmin(BaseModelView, model=Phrases):
    route = "phrases"
    name_plural = "Phrases"
    name = "Phrase"
    column_list = ["id", "ru", "en", "level", "topic"]
    column_searchable_list = ["ru", "en", "level"]
    column_filters = ["phrase"]
    column_sortable_list = ["ru", "en"]
    column_editable_list = ["ru", "en", "part_of_speech", "level", "topic"]


class RuleAdmin(BaseModelView, model=Rules):
    route = "rules"
    name_plural = "Rules"
    name = "Rule"
    column_list = ["id", "name", "description", "topic"]
    column_searchable_list = ["name"]
    column_filters = ["name"]
    column_sortable_list = ["name"]
    column_editable_list = ["rule", "topic"]


class FlowerView(BaseView):
    name = "Flower"
    icon = "fa-solid fa-seedling"

    @expose("/report", methods=["GET"])
    async def report_page(self, request):
        html_content = f"""
        <iframe src="{settings.BASE_URL[:-5]}:5555" style="width: 100%; height: 100%; border: none;"></iframe>
        """
        return HTMLResponse(content=Markup(html_content))
