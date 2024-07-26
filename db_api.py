from typing import Union
from create_db import Lake, DbSession
import create_db
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import text
from db_insert import insert_lake, update_lake
import json

app = FastAPI()


@app.get("/lakes")
def get_lakes_api():
    with DbSession() as db:
        lakes = db.query(Lake.id, Lake.name).all()
        lake_dict = {lake.id: lake.name for lake in lakes}
        return dict(sorted(lake_dict.items()))

@app.get("/lake/{lake_id}")
def get_lake_api(lake_id: int):
    with DbSession() as db:
        lake = db.query(Lake).\
        filter(Lake.id == lake_id).\
        all()
        lake = lake[0]
        return {
            "id": lake.id,
            "name": lake.name,
            "riparian_nations": lake.riparian_nations,
            "surface_area": lake.surface_area,
            "shorline": lake.shorline,
            "frozen_period": lake.frozen_period,
            "mean_depth": lake.mean_depth,
            "catchment_area": lake.catchment_area,
            "mixing_type": lake.mixing_type,
            "volume": lake.volume,
            "residence_time": lake.residence_time,
            "morphogenesis_or_dam": lake.morphogenesis_or_dam,
            "related_info_or_site": lake.related_info_or_site,
            "longitude": lake.longitude,
            "latitude": lake.latitude}

@app.post("/lake")
def add_lake_api(lake):
    lake = json.loads(lake)
    insert_lake(lake["name"], lake["riparian_nations"], lake["surface_area"], lake["shorline"], lake["frozen_period"],
                lake["mean_depth"], lake["catchment_area"], lake["mixing_type"], lake["volume"], lake["residence_time"],
                lake["morphogenesis_or_dam"], lake["related_info_or_site"], lake["longitude"], lake["latitude"])    
    return lake

@app.put("/lake/{lake_id}")
def update_lake_api(lake_id, lake):
    lake_id = int(lake_id)
    lake = json.loads(lake)
    update_lake(lake_id, lake.get("name"),  lake.get("riparian_nations"),  lake.get("surface_area"),  lake.get("shorline"),  lake.get("frozen_period"),
                 lake.get("mean_depth"),  lake.get("catchment_area"),  lake.get("mixing_type"),  lake.get("volume"),  lake.get("residence_time"),
                 lake.get("morphogenesis_or_dam"),  lake.get("related_info_or_site"), lake.get("longitude"), lake.get("latitude"))
    return get_lake_api(lake_id)

@app.delete("/lake/{lake_id}")
def delete_lake_api(lake_id):
    with DbSession() as db:
        lake = db.query(Lake).\
        filter(Lake.id == lake_id).\
        first()
        db.delete(lake)
        db.commit()
        return lake


