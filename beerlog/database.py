from sqlmodel import create_engine
from beerlog.config import settings
from beerlog import models

engine = create_engine(settings.database.url)

models.SQLModel.metadate.create_all(engine)