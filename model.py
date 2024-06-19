from pydantic import BaseModel


class CheckWordRequest(BaseModel):
    word: str


class CheckWordResponse(BaseModel):
    correct: bool
    table: list[list[str]]
    guessed: list[str] = []
    ip: str = ""
