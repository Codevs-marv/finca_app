from database.connection import SessionLocal
from models.movement import Movement
from models.movement_detail import MovementDetail
from models.supply import Supply


def register_entry(supply_id: int, quantity: float, reference: str = ""):
    db = SessionLocal()

    supply = db.query(Supply).get(supply_id)
    if not supply:
        raise Exception("Insumo no encontrado")

    movement = Movement(
        tipo="entrada",
        referencia=reference
    )
    db.add(movement)
    db.flush()

    detail = MovementDetail(
        movement_id=movement.id,
        supply_id=supply_id,
        cantidad=quantity
    )
    db.add(detail)

    supply.stock_actual += quantity

    db.commit()
    db.close()


def register_exit(supply_id: int, quantity: float, reference: str = ""):
    db = SessionLocal()

    supply = db.query(Supply).get(supply_id)
    if not supply:
        raise Exception("Insumo no encontrado")

    if supply.stock_actual < quantity:
        raise Exception("Stock insuficiente")

    movement = Movement(
        tipo="salida",
        referencia=reference
    )
    db.add(movement)
    db.flush()

    detail = MovementDetail(
        movement_id=movement.id,
        supply_id=supply_id,
        cantidad=quantity
    )
    db.add(detail)

    supply.stock_actual -= quantity

    db.commit()
    db.close()