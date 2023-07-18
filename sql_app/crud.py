from sqlalchemy.orm import Session

from . import models, schemas


def get_lead(db: Session, lead_id: int):
    return db.query(models.Lead).filter(models.Lead.id == lead_id).first()


def get_lead_by_phone(db: Session, phone_work: str):
    return db.query(models.Lead).filter(models.Lead.phone_work == phone_work).first()


def get_leads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lead).offset(skip).limit(limit).all()


def create_lead(db: Session, lead: schemas.LeadCreate):
    db_lead = models.Lead(phone_work=lead.phone_work, first_name=lead.first_name, last_name=lead.last_name)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


# def create_lead(db: Session, lead: models.LeadCreate):
#     db_lead = models.Lead(**lead.dict())
#     db.add(db_lead)
#     db.commit()
#     db.refresh(db_lead)
#     return db_lead
