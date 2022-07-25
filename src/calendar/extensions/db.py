from sqlmodel import create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def get_db():
    session = Session(engine)
    try:
        session.begin()
        yield session
    finally:
        session.close()
