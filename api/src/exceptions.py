from fastapi import HTTPException, status

TopicDoesntExist = HTTPException(status.HTTP_404_NOT_FOUND, "Topic doesn't exist")
TopicAlreadyExist = HTTPException(status.HTTP_409_CONFLICT, "Topic already exist")

OnlyCSVAreSupported = HTTPException(status.HTTP_400_BAD_REQUEST, "Only CSV files are supported.")
OnlyJSONAreSupported = HTTPException(status.HTTP_400_BAD_REQUEST, "Only JSON files are supported.")
InvalidTableSchema = HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid table schema")
InvlaidJSONFormat = HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid JSON format.")
