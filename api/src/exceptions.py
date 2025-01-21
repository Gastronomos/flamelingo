from fastapi import HTTPException, status


class EntityDoesntExist(HTTPException):

    def __init__(self, entity, status_code=status.HTTP_404_NOT_FOUND, detail="{} doesn't exist", headers=None):
        super().__init__(status_code, detail.format(entity), headers)


class EntityAlreadyExist(HTTPException):

    def __init__(self, entity, status_code=status.HTTP_409_CONFLICT, detail="{} already exist", headers=None):
        super().__init__(status_code, detail.format(entity), headers)


OnlyCSVAreSupported = HTTPException(status.HTTP_400_BAD_REQUEST, "Only CSV files are supported.")
OnlyJSONAreSupported = HTTPException(status.HTTP_400_BAD_REQUEST, "Only JSON files are supported.")
InvalidTableSchema = HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid table schema")
InvlaidJSONFormat = HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid JSON format.")
