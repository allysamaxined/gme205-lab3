import math
# For Programming Exercise 3, I'll be importing Shapely here.
from shapely.geometry import Point as ShapelyPoint

class Point:
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180.")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90.")

        self.id = id
        # self.lon = lon # This and self.lat will now be stored as a ShapelyPoint.
        # self.lat = lat
        self.geometry = ShapelyPoint(lon, lat)
        self.name = name
        self.tag = tag

# Preserving the access to Longitude and Latitude using Properties.
    @property
    def lon(self):
        return self.geometry.x

    @property
    def lat(self):
        return self.geometry.y
    
# ------------------------------------------------------------------ 
# Instance methods (behavior belongs to the object)
# ------------------------------------------------------------------

    def to_tuple (self) -> tuple [float, float]:
        """
        Return the coordinate as a (lon, lat) tuple.
        """
        return (self.lon, self.lat)
    def distance_to (self, other):
        return Point.haversine_m(self.lon, self.lat, other.lon, other.lat)

# ------------------------------------------------------------------ 
# Static method (pure spatial math)
# ------------------------------------------------------------------
    @staticmethod
    def haversine_m (
        lon1: float, lat1: float, lon2: float, lat2: float
        ) -> float:
        """
        Compute the Haversine distance between two lon/lat pairs in meters.
        
        Static method because it does not depend on object state.
        """
        R = 6_371_000 # Earth's radius in meters

        phi1 = math.radians (lat1)
        phi2 = math.radians (lat2)
        dphi = math.radians (lat2 - lat1)
        dlambda = math.radians (lon2 - lon1)

        a = (
            math.sin (dphi / 2) ** 2
            + math.cos (phi1)
            * math.cos (phi2)
            * math.sin (dlambda / 2) ** 2
        )

        c = 2 * math.atan2 (math.sqrt(a), math.sqrt(1 - a))
        return R * c

# ------------------------------------------------------------------ 
# Class method (constructing objects from data)
# ------------------------------------------------------------------
    @classmethod
    def from_row (cls, row):
        return cls (
            id = str(row ["id"]),
            lon = float(row ["lon"]),
            lat = float(row ["lat"]),
            name = row.get ("name"),
            tag = row.get ("tag"),
        )

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["id"],
            d["lon"],
            d["lat"],
            d.get("name"),
            d.get("tag")
        )

    def as_dict(self):
        return {
            "id" : self.id,
            "geometry" : [self.lon, self.lat],
            "name" : self.name,
            "tag" : self.tag,
            "bbox" : list(self.geometry.bounds)
        }

    def is_poi (self):
        return (self.tag or "").lower() == "poi"

# ------------------------------------------------------------------
# Creating the PointSet class to store multiple Point objects in a list.
# ------------------------------------------------------------------

class PointSet:
    def __init__ (self, points):
        self.points = points # PointSet is now outside of the Point class, and it is a separate class that can store multiple Point objects in a list.

    @classmethod
    def from_csv (cls, path):
        import pandas as pd 

        dataframe = pd.read_csv (path)
        points = []

        for _, row in dataframe.iterrows():
            try:
                point = Point.from_row (row)
                points.append (point)

            except ValueError:
                continue

        return cls (points)

    def count (self):
        return len (self.points) # Using the len() function to count the number of Point objects in the PointSet.
    def bbox (self):
        min_lon = min (point.lon for point in self.points)
        min_lat = min (point.lat for point in self.points)
        max_lon = max (point.lon for point in self.points)
        max_lat = max (point.lat for point in self.points)

        return (min_lon, min_lat, max_lon, max_lat)

    def filter_by_tag (self, tag):
        filtered_points = [
            point for point in self.points
            if (point.tag or "").lower() == tag.lower()
        ]

        return PointSet (filtered_points)
