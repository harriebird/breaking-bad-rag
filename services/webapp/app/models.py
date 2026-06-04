from datetime import datetime

from sqlmodel import AutoString, create_engine, Field, Session, SQLModel
from pgvector.sqlalchemy import VECTOR
from pydantic import HttpUrl
from typing import List

from core import config

class BaseModel(SQLModel):
    id : int | None = Field(default=None, primary_key=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=None, nullable=True)

class Paragraph(BaseModel, table=True):
    season: int | None = Field(default=None)
    episode: int | None = Field(default=None)
    title: str = Field(max_length=100)
    text: str = Field()
    embedding: List[float] = Field(sa_type=VECTOR(768))
    plot_url: HttpUrl | None = Field(sa_type=AutoString)

engine = create_engine(config.DB_URL)

def get_session():
    with Session(engine) as session:
        yield session