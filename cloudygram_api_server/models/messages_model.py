from typing import List, Dict
from pydantic import BaseModel

class DeleteMessagesRequest(BaseModel):
    message_ids: List[str] = None

class GetMessagesResponse(BaseModel):
    success: bool = True
    data: Dict[str, any]
