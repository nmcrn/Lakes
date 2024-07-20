import create_db
from create_db import Lake, Country
from sqlalchemy.sql import func
from create_db import Country, Lake


def country_largest_lake(country_name):
    with create_db.DbSession() as db:
        largest_lake = db.query(Lake).\
            join(Country).\
            filter(Country.name == country_name).\
            order_by(Lake.surface_area.desc()).\
            first()
        if largest_lake:
            return {
                'country': country_name,
                'lake_name': largest_lake.name,
                'surface_area': largest_lake.surface_area
            }
        
    print(largest_lake)

def max_depth_grater_then_400():
    with create_db.DbSession() as db:
        max_depth_lakes = db.query(Lake).\
        filter(Lake.mean_depth >= 7).\
        all()
        return [lake.name for lake in max_depth_lakes]
    
def country_total_lakes_volume(country):
    with create_db.DbSession() as db:
        lakes_in_country = db.query(Lake).\
        filter(Lake.riparian_nations == country).\
        all()
        total_volume = 0
        for lake in lakes_in_country:
            total_volume += lake.volume
        return total_volume
#Do it later with sqlalchemy sum function.


print(country_total_lakes_volume("Japan"))