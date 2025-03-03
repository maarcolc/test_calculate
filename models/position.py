from pydantic import BaseModel

class Position(BaseModel):
    entry_price: float
    stop_loss: float
    quantity: float
    leverage: int
    position: str
    model_config = {"extra": "forbid"}
    