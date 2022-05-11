import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

url_info = sqlalchemy.Table(
    "url_info",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("url", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.Integer),
    sqlalchemy.Column("content_type", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
