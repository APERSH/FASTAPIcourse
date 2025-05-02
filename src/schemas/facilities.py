from pydantic import BaseModel, ConfigDict

class Facilities(BaseModel):
    title: str

    model_config = ConfigDict(from_attributes=True)