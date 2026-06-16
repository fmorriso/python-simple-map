from typing import List, Tuple

# Define explicit type aliases for clarity
Coordinate = Tuple[float, float]          # [latitude, longitude]
BoundingBoxPolygon = List[Coordinate]     # A list of 4 or 5 coordinate pairs
