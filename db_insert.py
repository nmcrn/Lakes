import create_db

def insert_lake(name, riparian_nations, surface_area = None, shorline = None, frozen_period = None,
                mean_depth = None, catchment_area = None, mixing_type = None, volume = None, residence_time = None,
                morphogenesis_or_dam = None, related_info_or_site = None, longitude = None, latitude = None):
    with create_db.DbSession() as db:
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

def insert_country(name):
        with create_db.DbSession() as db:
            db.add(create_db.Country(name = name))
            
insert_lake("Lake Abashiri","Bulgeria", 33.0, 44.0, "Dec-Apr",7.2,1380.0,"Dimictic", 0.23,0.43)
# insert_lake("Lake Abaya","Ethiopia",1160.0,225.0,None,7.0,10000.0,None,8.2,7.7,"Natural")
# insert_lake("Abert Lake","USA",148.0,59.1,None,2.2,2125.0,None,0.33,4.5)
# insert_lake("Aberdeen Lake","Canada",1100.0,morphogenesis_or_dam= "Natural")
# insert_lake("Lake Abijata","Ethiopia",205.0,205.0,None, None,0.0016317,None,None,2.6)
# insert_lake("Abitibi","Canada",904.0,None,"Nov-May",3.0,None,"Dimictic",2.5,None,"Natural")
# insert_lake("Lake Abashiri","Japan",33.0,44.0,"Dec-Apr",7.2,1380.0,"Dimictic",0.23,0.43)

#insert_country("Bulgeria")
# insert_country("Japan")
# insert_country("Ethiopia")
# insert_country("USA")