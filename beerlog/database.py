import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

# from tkinter import E
from sqlmodel import create_engine, Session
from beerlog import models
from beerlog.config import settings

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)


def get_sessions():
    return Session(engine)
