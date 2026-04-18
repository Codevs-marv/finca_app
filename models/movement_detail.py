from sqlalchemy import Column, Integer, Float, ForeignKey
from database.connection import Base

class MovementDetail(Base):
    __tablename__ = "movement_details"

    id = Column(Integer, primary_key=True, index=True)
    movement_id = Column(Integer, ForeignKey("movements.id"))
    supply_id = Column(Integer, ForeignKey("supplies.id"))
    cantidad = Column(Float, nullable=False)

