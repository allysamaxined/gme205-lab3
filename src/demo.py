from spatial import Point
from spatial import Polygon
from spatial import Parcel

# p = Point("A", 121.0, 14.6, name="Gate", tag="POI")
# print(p.id)
# print(p.lon, p.lat)
# print(p.to_tuple())
# print(p.geometry.geom_type)

# test_dict = {
#     "id" : "Test",
#     # "lon" : 121.08, # This one is valid.
#     "lon" : 121.08, # This one is invalid.
#     "lat" : 14.5,
#     "name" : "Pasig River",
#     "tag" : "River"
# }
# p = Point.from_dict(test_dict)
# print(p.lon)

# print(p.as_dict())

# Testing the inherited behavior.

# p = Point("A", 121.0, 14.6)
# print(p.bbox())

# Testing parcel.

attributes = {
    "area" : 50.0,
    "zone" : "Residential",
    "is_active" : True
}

geom = Polygon ([
    (0,0),
    (10,0),
    (10,5),
    (0,5)
])

# Testing as_dict()
attributes = {
        "area" : 50.0,
        "zone" : "Residential",
        "is_active" : True
}

parcel = Parcel(101, geom, attributes)
# print(parcel.bbox())
# print(parcel.as_dict())

inside = Point("IN", 2, 2) 
outside = Point("OUT", 12, 2) 
 
print(inside.intersects(parcel))   # True 
print(outside.intersects(parcel))  # False 