from pydantic import BaseModel


class HealtCheck(BaseModel):
    environment: str
    title: str
    version: str
    description: str
