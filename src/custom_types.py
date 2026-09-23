# Custom types for use in this project.
# It follows PEP 613 guidelines for type aliases and is imported into main.py for use there.
# Requires python 3.12 or newer

type Coordinate = tuple[float, float]
type BoundingBoxPolygon = list[Coordinate]
