from sqlalchemy import Column, Integer, String, DateTime
from .database import db

from datetime import datetime


class Form_call(db.Model):

    __tablename__ = "form_call"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default=False)
    phone = Column(String, nullable=False, default=False)
    time = Column(String, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, phone, time):
        self.name = name
        self.phone = phone
        self.time = time
        self.created_at = datetime.now()
