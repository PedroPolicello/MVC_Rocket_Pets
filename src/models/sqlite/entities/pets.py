from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Pets [name={self.name}, type={self.type}]"
