# app/models.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class ReportIn(BaseModel):
    texto: str = Field(..., min_length=10)
    tipo_abuso: str = Field(..., description="Code interne ex: abuse_of_power")
    idioma: str = Field(..., regex="^(fr|es|en|sw|ln)$")
    source: Optional[str] = Field(None, description="web, mobile, partner")

class ReportOut(BaseModel):
    id: int
    message: str
    idioma: str
    created_at: datetime

class StatsOut(BaseModel):
    message: str
    total: int
    por_tipo: dict

# SQLAlchemy
from sqlalchemy import (
    Column, Integer, String, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True)
    texto = Column(Text, nullable=False)
    tipo_abuso = Column(String(64), nullable=False, index=True)
    idioma = Column(String(2), nullable=False, index=True)
    source = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)

class AbuseType(Base):
    __tablename__ = "abuse_types"
    code = Column(String(64), primary_key=True)
    # Optionnel si tu veux stocker les libellés en BD
    fr = Column(String(128)); es = Column(String(128))
    en = Column(String(128)); sw = Column(String(128)); ln = Column(String(128))
