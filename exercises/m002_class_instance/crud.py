from sqlalchemy import create_engine, Integer, String, select, update, delete, ForeignKey
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, Session, relationship
from typing import Optional, Dict, List


DB_URL = "postgresql+psycopg://postgres:Strongpassword1234@localhost:5432/shopdb"

engine = create_engine(DB_URL, echo=True, future=True)
Base = declarative_base()

def get_session():
    return Session(engine)

def init_schema():
    Base.metadata.create_all(engine)
    
    
    
class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"extend_existing":True }
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    type_of_products: Mapped[List["ProductType"]] = relationship(lazy = "selectin")
    extend_existing =True
    def __repr__(self) ->str: 
        return f"Product(id={self.id!r}) ,  name={self.name!r}, price={self.price!r})"
    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self.name, "price": int(self.price)}


class ProductType(Base):
    __tablename__ = "product_types"
    __table_args__ = {"extend_existing":True }
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    extend_existing =True
    def __repr__(self) ->str: 
        return f"Product(id={self.id!r}) ,  name={self.name!r})"
    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self.name, "id": self.id}
    products_id: Mapped[int] = mapped_column(ForeignKey("products_id"))

def create_product(name: str, price: int):
    with Session(engine) as s:
        obj  = Product(name = name, price=price) 
        s.add(obj)
        s.flush()
        s.commit()


def get_list_products():
    with Session(engine) as s:
        return [ p for p in s.scalars( select(Product)) ]
    
def get_product(product_id: int,engine) -> Optional[Product]:
    with Session(engine) as s:
        return s.get(Product,product_id)

def delete_product(product_id: int) -> int:
    with Session(engine) as s:
        result = s.execute(delete(Product).where(Product.id == product_id))
        s.commit()