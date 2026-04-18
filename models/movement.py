from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.connection import Base

class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    referencia = Column(String)
    nota = Column(String)

