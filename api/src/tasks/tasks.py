from api.src.settings import settings
from api.src.tasks.celery import celery


@celery.task
def verification_flow(code: str, user: dict, name: str, template: str):
    if settings.DEBUG:
        print(f"Your code is {code}")
    else:
        settings.email.send_mail(
            user["email"],
            settings.templates.get_template(template).render({"code": code}),
            name,
            True,
        )
