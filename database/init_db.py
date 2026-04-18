from database.connection import engine, Base

#Importar modelos para que SQLAlchemy los registre
from models.supply import Supply
from models.movement import Movement
from models.movement_detail import MovementDetail

def init_db():
    Base.metadata.create_all(bind=engine)

