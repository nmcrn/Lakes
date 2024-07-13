# first_try
    # from sqlalchemy import Column, Integer, String, create_engine
    # from sqlalchemy.orm import declarative_base


    # db_url = "sqlite:///Lakes/database.db"

    # engine = create_engine(db_url)

    # Base = declarative_base()

    # class User(Base):
    #     __tablename__ = "users"

    #     id = Column(Integer, primary_key=True)
    #     name = Column(String)
    #     age = Column(Integer)

    # Base.metadata.create_all(engine)

# from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship
# from Lakes.create_db import Lake,Country,Lake_Metadata

# DATABASE_URL = "sqlite:///database.db"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db = SessionLocal()

# # country1 = Country(name="Country A")
# # country2 = Country(name="Country B", riparian_nation = 1)

# lake1 = Lake(name="Lake 1", country_id=1, mean_depth=500)
# lake2 = Lake(name="Lake 2", country_id=1, mean_depth=300)
# lake3 = Lake(name="Lake 3", country_id=2, mean_depth=700)

# # metadata1 = Lake_Metadata(lake_id=1, metadata_key="type", metadata_value="freshwater")
# # metadata2 = Lake_Metadata(lake_id=2, metadata_key="type", metadata_value="brackish")
# # metadata3 = Lake_Metadata(lake_id=3, metadata_key="type", metadata_value="saltwater")

# # db.add_all([country1, country2, lake1, lake2, lake3, metadata1, metadata2, metadata3])
# db.add_all([lake1, lake2, lake3])
# db.commit()
# db.close()

