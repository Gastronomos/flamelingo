from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status

from api.src.controllers.users import get_current_superuser
from api.src.dao.topics import TopicsDAO
from api.src.exceptions import TopicAlreadyExist, TopicDoesntExist
from api.src.schemas.topics import CreateTopic, DisplayTopic, UpdateTopic
from api.src.schemas.users import DisplayUser
from api.src.utils.utils import process_csv_file, process_json_file

router = APIRouter(prefix="/topics", tags=["topics"])


@router.get("")
async def get_topics(name: str | None = None, limit: int | None = 50, offset: int | None = 0) -> list[DisplayTopic]:
    return await TopicsDAO.find_all(name=name, limit=limit, offset=offset)


@router.get("/{topic_id}")
async def get_topic_by_id(topic_id: UUID) -> DisplayTopic:
    existed_topic = await TopicsDAO.find_by_id(topic_id)
    if not existed_topic:
        raise TopicDoesntExist
    return existed_topic


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_topic(data: CreateTopic, user: DisplayUser = Depends(get_current_superuser)) -> DisplayTopic:
    topic = await TopicsDAO.find_one_or_none(name=data.name)
    if topic:
        raise TopicAlreadyExist
    return await TopicsDAO.add(**data.model_dump())


@router.post("/import/csv", status_code=status.HTTP_201_CREATED)
async def import_csv_topics(file: UploadFile, user: DisplayUser = Depends(get_current_superuser)) -> list[DisplayTopic]:
    return await process_csv_file(file, CreateTopic, TopicsDAO)


@router.post("/import/json", status_code=status.HTTP_201_CREATED)
async def import_csv_topics(file: UploadFile, user: DisplayUser = Depends(get_current_superuser)) -> list[DisplayTopic]:
    return await process_json_file(file, CreateTopic, TopicsDAO)


@router.patch("/{topic_id}")
async def update_topic(topic_id: UUID, data: UpdateTopic, user: DisplayUser = Depends(get_current_superuser)) -> DisplayTopic:
    topic = await TopicsDAO.find_one_or_none(name=data.name)
    if not topic:
        raise TopicDoesntExist
    return await TopicsDAO.update(topic_id, **data.model_dump())


@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_topic(topic_id: UUID, user: DisplayUser = Depends(get_current_superuser)):
    await TopicsDAO.delete(topic_id)
