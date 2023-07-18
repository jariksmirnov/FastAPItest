from pydantic import BaseModel


class LeadBase(BaseModel):
    phone_work: str
    first_name: str
    last_name: str


class LeadCreate(LeadBase):
    phone_work: str


class Lead(LeadBase):
    id: int

    class Config:
        from_attributes = True
