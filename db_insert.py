import create_db
from create_db import Lake, Country

def insert_lake(name, riparian_nations, surface_area = None, shorline = None, frozen_period = None,
                mean_depth = None, catchment_area = None, mixing_type = None, volume = None, residence_time = None,
                morphogenesis_or_dam = None, related_info_or_site = None, longitude = None, latitude = None):
    with create_db.DbSession() as db:
        country = db.query(Country).filter(Country.name == riparian_nations).first()
        if not country:
            insert_country(riparian_nations)
            country = db.query(Country).filter(Country.name == riparian_nations).first()
        db.add(create_db.Lake(name = name,
                              riparian_nations = riparian_nations, 
                              surface_area = surface_area, 
                              shorline = shorline, 
                              frozen_period = frozen_period, 
                              mean_depth = mean_depth,
                              catchment_area = catchment_area,
                              mixing_type = mixing_type,
                              volume = volume,
                              residence_time = residence_time,
                              morphogenesis_or_dam = morphogenesis_or_dam,
                              related_info_or_site = related_info_or_site,
                              longitude = longitude,
                              latitude = latitude))
        db.commit

def update_lake(id, name = None, riparian_nations = None, surface_area = None, shorline = None, frozen_period = None,
                mean_depth = None, catchment_area = None, mixing_type = None, volume = None, residence_time = None,
                morphogenesis_or_dam = None, related_info_or_site = None, longitude = None, latitude = None):
    with create_db.DbSession() as db:
        country = db.query(Country).filter(Country.name == riparian_nations).first()
        if not country:
            insert_country(riparian_nations)
            country = db.query(Country).filter(Country.name == riparian_nations).first()
        update_data = {}
        if name is not None:
            update_data[Lake.name] = name
        if riparian_nations is not None:
            update_data[Lake.riparian_nations] = riparian_nations
        if surface_area is not None:
            update_data[Lake.surface_area] = surface_area
        if shorline is not None:
            update_data[Lake.shorline] = shorline
        if frozen_period is not None:
            update_data[Lake.frozen_period] = frozen_period
        if mean_depth is not None:
            update_data[Lake.mean_depth] = mean_depth
        if catchment_area is not None:
            update_data[Lake.catchment_area] = catchment_area
        if mixing_type is not None:
            update_data[Lake.mixing_type] = mixing_type
        if volume is not None:
            update_data[Lake.volume] = volume
        if residence_time is not None:
            update_data[Lake.residence_time] = residence_time
        if morphogenesis_or_dam is not None:
            update_data[Lake.morphogenesis_or_dam] = morphogenesis_or_dam
        if related_info_or_site is not None:
            update_data[Lake.related_info_or_site] = related_info_or_site
        if longitude is not None:
            update_data[Lake.longitude] = longitude
        if latitude is not None:
            update_data[Lake.latitude] = latitude
        db.query(Lake).filter(Lake.id == id).update(update_data)
        db.commit()

def insert_country(name):
    with create_db.DbSession() as db:
        db.add(create_db.Country(name = name))