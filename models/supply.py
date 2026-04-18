from sqlalchemy import Column, Integer, String, Float
from database.connection import Base

class Supply(Base):
    __tablename__ = "supplies"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    unidad = Column(String, nullable=False)
    stock_actual = Column(Float, default=0)

