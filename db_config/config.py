import configparser

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from config import conf_path

config = configparser.ConfigParser()
config.read(conf_path)

drivername = config.get('database', 'drivername')
username = config.get('database', 'username')
password = config.get('database', 'password')
host = config.get('database', 'host')
port = config.get('database', 'port')
database = config.get('database', 'database')

url = URL.create(
    drivername=drivername,
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

print(url)
engine = create_engine(url, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
else:
    engine.connect()

Session = sessionmaker(bind=engine)
Base = declarative_base()