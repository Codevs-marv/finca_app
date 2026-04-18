from database.init_db import init_db

if __name__ == "__main__":
    print("Inicializando base de datos...")
    init_db()
    print("Base de datos lista.")

from services.movement_service import register_entry, register_exit

# Crear entrada
register_entry(supply_id=1, quantity=20, reference="Compra")

# Crear salida
register_exit(supply_id=1, quantity=10, reference="Uso en ganado")

print("Movimientos ejecutados correctamente")