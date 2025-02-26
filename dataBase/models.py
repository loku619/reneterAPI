from pydantic import BaseModel, Field
from datetime import datetime

class RenterData(BaseModel):
    name: str
    room_No: int
    room_Rent: int
    rent_Paid: str
    amount_Paid: int
    balance_Amount: int
    curr_Electric_Unit: int
    prev_Electric_Unit: int
    per_Unit: int
    electric_Bill: int
    status: str
    month: str
    paid_On: str
    updated_at: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))
    creation: int = Field(default_factory=lambda: int(datetime.timestamp(datetime.now())))
