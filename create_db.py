from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, scoped_session

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Lake(Base):
    __tablename__ = "lakes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    riparian_nations = Column(String, ForeignKey("countries.name"))
    surface_area = Column(Float)  #square km
    shorline = Column(Float) #km
    frozen_period = Column(String)
    mean_depth = Column(Float) #meters
    catchment_area = Column(Float) #square km
    mixing_type = Column(String)
    volume = Column(Float)
    residence_time = Column(Float)
    morphogenesis_or_dam = Column(String)
    related_info_or_site = Column(String)
    country = relationship("Country")

class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String, index=True)
    riparian_nation = Column(String)
    surface_area = Column(Integer)
    shoreline = Column(Integer)
    frozen_period = Column(Integer)
    related_info_or_site = Column(String)
    mean_depth = Column(Integer)
    catchment_area = Column(Integer)
    mixing_type = Column(String)
    volume = Column(Integer)
    residence_time = Column(Integer)
    morphogenesis_or_dam = Column(String)
    
class Lake_Metadata(Base):
    __tablename__ = "lake_metadata"
    id = Column(Integer, primary_key=True, index=True)
    lake_name = Column(String, ForeignKey("lakes.name"))
    metadata_key = Column(String)
    metadata_value = Column(String)
    lake = relationship("Lake")

Base.metadata.create_all(engine)

class DbSession:
    def __init__(self):
        pass

    def __enter__(self):
        self.connection = engine.connect() #Reuse the engine instead of creating a new one
        self.session = scoped_session(\
                sessionmaker(\
                autocommit=False,\
                autoflush=False,\
                bind=engine))
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.commit()
        self.session.close()
        self.connection.close()