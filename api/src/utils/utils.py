import csv
import json
from io import StringIO

from fastapi import UploadFile
from pydantic import BaseModel

from api.src.dao.base import BaseDAO
from api.src.exceptions import InvalidTableSchema, InvlaidJSONFormat, OnlyCSVAreSupported, OnlyJSONAreSupported


async def process_csv_file(file: UploadFile, create_schema: BaseModel, dao: BaseDAO):
    if not file.content_type == "text/csv":
        raise OnlyCSVAreSupported

    content = await file.read()
    csv_content = StringIO(content.decode("utf-8"))
    reader = csv.DictReader(csv_content)

    records = []
    for row in reader:
        if not all(field in row for field in create_schema.model_fields.keys()):
            raise InvalidTableSchema

        record_data = create_schema(**row).model_dump()
        records.append(record_data)

    return await dao.add_all(records)


async def process_json_file(file: UploadFile, create_schema: BaseModel, dao: BaseDAO):
    if not file.content_type == "application/json":
        raise OnlyJSONAreSupported

    content = await file.read()

    try:
        json_data = json.loads(content)
    except json.JSONDecodeError:
        raise InvlaidJSONFormat

    if not isinstance(json_data, list):
        raise InvlaidJSONFormat

    records = []
    for row in json_data:
        if not all(field in row for field in create_schema.model_fields.keys()):
            raise InvalidTableSchema

        record_data = create_schema(**row).model_dump()
        records.append(record_data)

    return await dao.add_all(records)
