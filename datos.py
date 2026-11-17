from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)


# =====================================
# ORM 1 - CONFIGURACION DE LA CONEXION
# =====================================

# El archivo inventario.db se crea en la carpeta de ejecucion
# la primera vez que se abre una conexion.
motor = create_engine("sqlite:///inventario.db")


# =====================================
# ORM 2 - CLASE BASE
# =====================================

class Base(DeclarativeBase):
    pass


# =====================================
# ORM 3 - MODELO CALZADO
# =====================================

class Calzado(Base):
    __tablename__ = "calzados"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    modelo: Mapped[str] = mapped_column(String)
    talla: Mapped[int]
    precio: Mapped[float]

    def __repr__(self):
        return (f"Calzado(id={self.id}, modelo={self.modelo!r}, "
                f"talla={self.talla}, precio={self.precio})")


# =====================================
# ORM 4 - CREAR LA TABLA
# =====================================

def iniciar_bd():
    # Crea la tabla calzados solo si no existe (no borra datos).
    Base.metadata.create_all(motor)


# =====================================
# ORM 5 - REGISTRAR CALZADO
# =====================================

def registrar_calzado(modelo, talla, precio):
    nuevo = Calzado(modelo=modelo, talla=talla, precio=precio)
    with Session(motor) as sesion:
        sesion.add(nuevo)
        sesion.commit()
    return True


# =====================================
# ORM 6 - LISTAR CALZADOS
# =====================================

def obtener_calzados():
    with Session(motor) as sesion:
        return list(sesion.scalars(select(Calzado).order_by(Calzado.id)))


# =====================================
# ORM 7 - BUSCAR POR ID
# =====================================

def obtener_calzado(id_calzado):
    with Session(motor) as sesion:
        return sesion.get(Calzado, id_calzado)  # objeto o None


# =====================================
# ORM 8 - ACTUALIZAR PRECIO
# =====================================

def modificar_precio(id_calzado, nuevo_precio):
    with Session(motor) as sesion:
        calzado = sesion.get(Calzado, id_calzado)
        if calzado is None:
            return False
        calzado.precio = nuevo_precio
        sesion.commit()
        return True


# =====================================
# ORM 9 - ELIMINAR CALZADO
# =====================================

def borrar_calzado(id_calzado):
    with Session(motor) as sesion:
        calzado = sesion.get(Calzado, id_calzado)
        if calzado is None:
            return False
        sesion.delete(calzado)
        sesion.commit()
        return True
