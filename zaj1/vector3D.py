import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D = ({self.x}, {self.y}, {self.z})"

    def change(self, dx, dy, dz):
        self.x = dx
        self.y = dy
        self.z = dz

    def getDim(self):
        return [self.x, self.y, self.z]

    def norm(self):
        return math.sqrt(self.x ^ 2 + self.y ^ 2 + self.z ^ 2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, no):
        return Vector3D(self.x * no, self.y * no, self.z * no)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    @staticmethod
    def are_orthogonal(self, other):
        if self.x * other.x + self.y * other.y + self.z * other.z == 0:
            return True

    