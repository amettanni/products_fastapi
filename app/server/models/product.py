from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Dict

class ProductModel(BaseModel):

    name: str = Field(...)
    description: str = Field(...)
    parameters: Optional[List[Dict]] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "IPhone 11",
                "description": "Released 2019, September 20 · 194g, 8.3mm thickness",
                "parameters": [
                    {
                        "camera":"12MP"
                    },
                    {
                        "memory":64
                    },
                ],
            }
        }



def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
