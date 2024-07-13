import create_db

def insert_lake(id, name, riparian_nations, surface_area = None, shorline = None, frozen_period = None,
                mean_depth = None, catchment_area = None, mixing_type = None, volume = None, residence_time = None,
                morphogenesis_or_dam = None, related_info_or_site = None):
    with create_db.DbSession() as db:
        db.add(create_db.Lake(name = name,
                              id = id,
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
                              related_info_or_site = related_info_or_site))

insert_lake(1, "Shizafon", "Israel")