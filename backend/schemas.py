from pydantic import BaseModel

class ToDoRequest(BaseModel):
    name: str
    completed: bool = False

class ToDoResponse(BaseModel):
    name: str
    completed: bool
    id: int

    class Config:
        orm_mode = True