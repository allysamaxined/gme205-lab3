from src.spatial import Point, Parcel
from shapely.geometry import Polygon
import json

# To run the focused tests, use: python -m tests.test_spatial

# Focused Tests
# Valid Point
p = Point("A", 121.0, 14.6)
print("Valid Point:", p.id, p.lon, p.lat)


# Invalid longitude must raise ValueError.
try:
    invalid = Point("BAD", 999, 14.6)
except ValueError as error:
    print("Invalid Point:", error)


# Valid from_dict must create a Point.
valid_record = {
    "id": "B",
    "lon": 121.0,
    "lat": 14.6
}

p2 = Point.from_dict(valid_record)
print("Valid from_dict:", p2.as_dict())


# Invalid from_dict must fail after running through the validation.
invalid_record = {
    "id": "BAD",
    "lon": 999,
    "lat": 14.6
}

try:
    Point.from_dict(invalid_record)
except ValueError as error:
    print("Invalid from_dict:", error)


# Point bounding box should return correctly.
print("Point bbox:", p.bbox())


# Create Parcel.
geom = Polygon([
    (0, 0),
    (20, 0),
    (20, 10),
    (0, 10)
])

attributes = {
    "area": 200.0,
    "zone": "Commercial",
    "is_active": True
}

parcel = Parcel(101, geom, attributes)


# Parcel bounding box should return correctly.
print("Parcel bbox:", parcel.bbox())


# Testing intersections.
inside = Point("IN", 10, 5)
outside = Point("OUT", 15, 25)

print("Inside intersects:", inside.intersects(parcel))
print("Outside intersects:", outside.intersects(parcel))

# Produce a JSON-ready output.
print("Point JSON:", json.dumps(inside.as_dict()))
print("Parcel JSON:", json.dumps(parcel.as_dict()))