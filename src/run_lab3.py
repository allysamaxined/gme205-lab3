from spatial import Point, Parcel
from shapely.geometry import Polygon
import json
import matplotlib.pyplot as plt

def main():
    # Creating a rectangular polygon.

    geom = Polygon ([
        (0,0),
        (20,0),
        (20,10),
        (0,10)
    ])

    # Creating attributes.

    attributes = {
        "area" : 200.0,
        "zone" : "Commercial",
        "is_active" : True
    }

    # Creating the Parcel.

    parcel = Parcel(202620920, geom, attributes)

    # Creating Points inside and outside the rectangle and printing the result.

    inside = Point("IN", 10, 5, name="Inside Point", tag="POI")
    outside = Point("OUT", 15, 25, name="Outside Point", tag="POI")

    # Creating the report.

    report = {
        "point" : inside.as_dict(),
        "parcel": parcel.as_dict(),
        "relationships" : {
            "inside_intersects_parcel" : inside.intersects(parcel),
            "outside_intersects_parcel" : outside.intersects(parcel)
        }
    }

    # Generating the report.

    with open ("output/lab3_report.json", "w") as file:
        json.dump (report, file, indent = 4)

    # Visualizing the parcel polygon, inside, and outside points.

    x, y = parcel.geometry.exterior.xy
    plt.plot(x, y, label = "Parcel")

    plt.scatter(inside.lon, inside.lat, label="Inside Point")
    plt.scatter(outside.lon, outside.lat, label="Outside Point")

    plt.annotate (
        "Inside Point",
        (inside.lon, inside.lat),
        xytext=(5, 5),
        textcoords="offset points")
    
    plt.annotate(
        "Outside Point",
        (outside.lon, outside.lat),
        xytext=(5, -12),
        textcoords="offset points")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Demonstration of Parcel and Point Intersection")

    plt.legend(
        title = "Object",
        fontsize = 8,
        title_fontsize = 9,
        markerscale = 0.7
    )

    plt.savefig("output/lab3_preview.png")

    plt.close()

if __name__ == "__main__":
    main()