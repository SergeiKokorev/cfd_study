from __future__ import annotations
from settings import *


@dataclass
class Point:
    _x: int
    _y: int
    _z: int

    @property
    def point(self):
        return np.array([self._x, self._y, self._z])
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, x: float):
        if not isinstance(x, int | float):
            raise ValueError(f'X coordinate must be integer or float type. Given {type(x)}')
        self._x = x

    @x.setter
    def y(self, y: float):
        if not isinstance(y, int | float):
            raise ValueError(f'X coordinate must be integer or float type. Given {type(y)}')
        self._y = y

    @z.setter
    def z(self, z: float):
        if not isinstance(z, int | float):
            raise ValueError(f'X coordinate must be integer or float type. Given {type(z)}')
        self._z = z

    def __getitem__(self, i: int):
        if not isinstance(i, int):
            raise IndexError('Index must be integer type')
        if i >= 3:
            raise IndexError(f'Index out of range.')
        return self.point[i]

    def __setitem__(self, i: int, b: float | int):
        if not isinstance(i, int):
            raise IndexError('Index must be integer type')
        if not isinstance(b, float | int):
            raise ValueError(f'Value must be float or integer type. Given {type(b)}')
        if i >= 3:
            raise IndexError(f'Index out of range.')
        if i == 0:
            self._x = b
        elif i == 1:
            self._y = b
        elif i == 2:
            self._z = b

    def __add__(self, point) -> Point:
        
        if not isinstance(point, Point):
            raise ValueError(f'Unsupported operand + for {type(point) and type(self.__class__.__name__)}')

        return Point(self._x + point.x, self._y + point.y, self._z + point.z)

    def __radd__(self, point: Point) -> Point:
        return self.__add__(point)
    
    def __iadd__(self, point: Point) -> Point:
        return self.__add__(point)

    def __mul__(self, val: Point | float):
        
        if not isinstance(val, Point | float | int):
            raise ValueError(f'Unsupported operand * for {type(val) and type(self.__class__.__name__)}')
        
        if isinstance(val, int | float):
            return Point(self._x * val, self._y * val, self._z * val)
        
        return Point(self._y * val.z - self._z * val.y, self._z * val.x - self._x * val.z, self._x * val.y - self._y * val.x)

    def __rmul__(self, val: Point | float) -> Point:

        if not isinstance(val, Point| int | float):
            raise ValueError(f'Unsupported operand * for {type(val) and type(self.__class__.__name__)}')

        if isinstance(val, float | int):
            return self.__mul__(val)
        
        return Point(self._z * val.y - self._y * val.z, self._x * val.z - self._z * val.x, self._y * val.x - self._x * val.y)

    def __imul__(self, val: Point | float) -> Point:
        return self.__mul__(val)

    def __matmul__(self, val: Point | float) -> Point | float:
        if not isinstance(val, Point | float | int):
            raise ValueError(f'Unsupported operand @ for {type(val) and type(self.__class__.__name__)}')
        if isinstance(val, Point):
            return self._x * val.x + self._y * val.y + self._z * val.z
        if isinstance(val, int | float):
            return Point(self._x * val, self._y * val, self._z * val)

    def __str__(self):
        return f'{self.__class__.__name__}(x={self._x}, y={self._y}, z={self._z})'



@dataclass
class Triangle:
    p1: Point
    p2: Point
    p3: Point


if __name__ == "__main__":

    p1 = Point(1, 2, 0)
    p2 = Point(2, 2, 0)
    p2[1] = 6
