# Programming Exercise 3
## Spatial Object Systems in Python

#### Introduction to the Programming Exercise
This programming exercise focuses on refactoring a spatial object model while preserving meaning and responsibility. This will not rewrite what's already built from Laboratory/Programming Exercise 2, rather, it will build from the previous object model by refactoring the Point class. The present Laboratory/Programming Exercise introduces SpatialObject, Point, and Parcel. The core idea is to *change the implementation without losing the object's meaning.*

#### Materials/Requirements
1. Python
2. VS Code
3. Git/GitHub
4. Shapely

#### Python Libraries Used
1. pandas
2. matplotlib
3. json
4. math

#### Project Structure
The structure of the project is presented as follows:

gme205-lab3
    data
        points.csv
    output
        lab3_preview.png
        lab3_report.json
    src
        demo.py
        run_lab3.py
        spatial.py
    tests
        test_spatial.py
    .gitignore
    README.md
    requirements.txt

#### Environment Setup
1. Create the root directory.
2. Open VS Code, open the root folder, and create the virtual environment (venv).
3. Activate the venv using:
    .venv\Scripts\activate
4. Install required dependencies.
    pip install --upgrade pip
    pip install pandas matplotlib
    pip freeze > requirements.txt
5. (.venv) Must be activated, commands must be executed from the root directory.

#### Running the Program
To demonstrate or check the SpatialObject, Parcel, the inherited behavior, and the intersection, run:
    python src/demo.py

    demo.py performs the demonstrations of how the object behaves.

To generate outputs (.png preview and .json report), run:
    python src/run_lab3.py

    This is the runner script. It generates the final JSON report and the PNG visualization/image of the project.

To verify or test, run:
    python -m tests.test_spatial

    This performs the required focused verification.

*Note: data/points.csv does not contain the point coordinates or locations. It was maintained to follow the project structure; the demonstration points are in src/demo.py. The points used for the final outputs are in src/run_lab3.py.*

#### Project Output
After executing or running the program, specifically python src/run_lab3.py, the following outputs will be created:
1. A visualization of points with a parcel, identifying inside and outside point locations stored as 'lab3_preview.png.'
2. A JSON report containing the serialized Point and Parcel information and their intersection relationships.

### Reflections
1. **Refactoring: What changed in the internal representation of Point? What remained stable for code using the object?**
In Laboratory/Programming Exercise 2 or Lab 2, Point stored the longitude and latitude values directly as its attributes. However, in Lab 3, the internal representation changed: those coordinates are now stored in a ShapelyPoint passed to the SpatialObject constructor. The object can still access point.lon and point.lat through code.

Other methods that remained available were the validation of coordinates, the to_tuple(), and the Haversine distance_to(). The internal or implementation changed; it's the public meaning and interface of Point that remained stable.

2. **Responsibility: Which behavior now belongs to Shapely, which belongs to SpatialObject, and which remains specific to Point or Parcel?**
Shapely now handles the representation of geometry, as well as performing geometric operations. SpatialObject stores them and provides the behavior shared by spatial objects (Point and Parcel), such as the bbox() and intersects(). 

Point still has the validation of coordinates, calculations, and  methods on its own; in short, it remains responsible for its own identity. The same goes for Parcel, storing its own parcel ID and other structured attributes. Both inherit the shared spatial behavior from SpatialObject.

3. **Data Boundary: Why should from_dict() delegate validation to the constructor?**
It should delegate validation to the constructor to ensure a single validation boundary. It is from_dict()'s responsibility to read the values from the dictionary, and then use them to construct a valid Point, such as by checking coordinates.

By delegating this, it prevents duplication of validation rules across the process, and ensures that the direct construction and dictionary-based constructon accept and reject the same values.

4. **Output Boundary**: Why should as_dict() return primitive/JSON-ready values rather than Shapely geometry objects?
It should return primitive/JSON-ready values, rather than Shapely geometry objects, because they can be serialized to JSON. A standard JSON won't be able to directly represent a live Shapely geometry object, and would reveal the structure or internal implementation of the class. This can help return information, such as coordinates and bbox() as lists that can be used by others for inspection or analysis without needing to use Shapely.

5. **Inheritance**: Why does intersects() belong in SpatialObject instead of being duplicated in Point and Parcel?
It will be redundant and won't be a good design. In OOP, we think in a way that we will assign behaviors to objects based on how we understand them to act or behave. Adding it in both Point and Parcel will make them both do methods that would make them handle more than they should be handling. 

Additionally, it belongs in SpatialObject because the intersection behavior is shared by any object that has geometry. 

This can also help during instances where behaviors need changing, it can be updated in one place.

6. **Coordinate Meaning**: Why is geometry.distance() not automatically a real-world distance in meters for longitude and latitude data?
Geometry.distance() calculates straight-line Cartesian distance between two geometries using the units of their input coordinates. It is planar; it analyzes geometries in a Cartesian plane and does not transform coordinate systems. If this is used with longitude and latitude coordinates, the results will be expressed in coordinate degrees, rather than real-world meters. This is also why the Haversine method remains, to estimate distance in real-world measurements while also accounting for the curvature of the Earth's surface.

7. **Scale**: If the system grows to millions of objects, what part of this design helps maintainability, and what performance problems would still require different techniques?
Should the system grow to millions of objects, the separation of responsibilities will greatly help with maintaining how it runs stably. The shared behavior is defined once in SpatialObject, while Point and Parcel contain their own domain-specific responsibilities. The structured from_dict() and as_dict() boundaries also make it easier to change how data enters and leaves the system without rewriting the domain classes.

If it grows to millions of objects, it could create memory, processing, intersection-search, and output visualization problems. While Shapely helps by providing geometric operations, it might not perform well by itself in a large-scale implementation. Handling this scale could require spatial indexing, spatial databases, batch or chunked processing, and simplified or aggregated visualizations.