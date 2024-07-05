from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class Lake(Base):
    __tablename__ = "lakes"
    id = Column(Integer, primary_key=True)
    lake_name = Column(String)
    riparian_nations = Column(String)
    surface_area_in_sq_km = Column(Integer)  #Km^2
    shorline_in_km = Column(Integer)
    frozen_period = Column(String)
    mean_depth_in_m = Column(Integer)
    catchment_area_in_sq_km = Column(Integer)
    mixing_type = Column(Integer)
    volume = Column(Integer)
    residence_time = Column(Integer)
    morphogenesis_or_dam = Column(String)
    related_info_or_site = Column(String)


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Lake_Metadata(Base):
    __tablename__ = "lake_metadata"
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)