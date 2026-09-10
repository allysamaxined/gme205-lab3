from spatial import Point

# p = Point("A", 121.0, 14.6, name="Gate", tag="POI")
# print(p.id)
# print(p.lon, p.lat)
# print(p.to_tuple())
# print(p.geometry.geom_type)

test_dict = {
    "id" : "Test",
    # "lon" : 121.08, # This one is valid.
    "lon" : 121.08, # This one is invalid.
    "lat" : 14.5,
    "name" : "Pasig River",
    "tag" : "River"
}
p = Point.from_dict(test_dict)
print(p.lon)

print(p.as_dict())

# Testing the inherited behavior.

p = Point("A", 121.0, 14.6)
print(p.bbox())