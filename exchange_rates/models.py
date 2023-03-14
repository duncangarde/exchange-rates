from sqlalchemy import BigInteger, String, Date, JSON, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SourceExchangeRateResponses(Base):
    __tablename__ = "source__exchange_rate_responses"
    timestamp = Column(BigInteger, primary_key=True, nullable=False)
    base = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    rates = Column(JSON, nullable=True)
