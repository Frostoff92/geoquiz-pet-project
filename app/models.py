from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class CountryModel(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    flag: Mapped[str] = mapped_column(String, nullable=False)
    difficulty: Mapped[str] = mapped_column(String, nullable=False)
    similar_to: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    continent: Mapped[str] = mapped_column(String, nullable=False)
    capital: Mapped[str] = mapped_column(String, nullable=False)
    