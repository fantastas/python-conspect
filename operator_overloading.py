from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Vector:
    x: float
    y: float

    # overloading division
    def __truediv__(self, other: float) -> Vector:
          return Vector(self.x / other, self.y / other)
    
    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

def main() -> None:
    # float type also accepts int
    point = Vector(1, 2)
    # / not supported for type vector
    print(point / 2)
    print(point + point)
    # Can combine operations
    print(point + point / 2)



if __name__ == "__main__":
    main()
