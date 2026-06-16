# Custom types for use in this project.
# It follows PIE 613 guidelines for type aliases and is imported into main.py for use there.

from typing import TypeAlias

Coordinate: TypeAlias = tuple[float, float]
BoundingBoxPolygon: TypeAlias = list[Coordinate]
