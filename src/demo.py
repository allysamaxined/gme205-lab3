from spatial import Point, Parcel
from shapely.geometry import Polygon

p = Point("A", 121.0, 14.6, name="Gate", tag="POI")
print(p.id)
print(p.lon, p.lat)
print(p.to_tuple())
print(p.geometry.geom_type)

# Testing the inherited behavior.
print(p.bbox())

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

parcel = Parcel(101, geom, attributes)
print(parcel.bbox())
print(parcel.as_dict())

# Testing intersections.
inside = Point("IN", 2, 2) 
outside = Point("OUT", 12, 2) 
 
print(inside.intersects(parcel))   # True 
print(outside.intersects(parcel))  # False 