from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insert(data, table, pg_connection_string) -> None:
    """
    Inserts data into the given table in the database
    """
    engine = create_engine(pg_connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = table(**data)
    session.add(row)
    session.commit()
