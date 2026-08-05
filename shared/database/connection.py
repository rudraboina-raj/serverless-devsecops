from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from shared.core.settings import Settings

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=Settings.DB_USERNAME,
    password=Settings.DB_PASSWORD,
    host=Settings.DB_HOST,
    port=Settings.DB_PORT,
    database=Settings.DB_NAME,
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)