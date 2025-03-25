import math 

class Vector:
    def __init__(self, *comp):
        self.comp = tuple(comp)

    def __repr__(self):
        return f"Vector{self.comp}"

    def __add__(self, second):
        if not isinstance(second, Vector):
            print("not the same type")
        if len(self.comp) != len(second.comp):
            print("not the same dimenstion")
        return Vector(*(a + b for a, b in zip(self.comp, second.comp)))
        
    def __sub__ (self, second):
        if not isinstance(second, Vector):
            print("not the same type")
        if len(self.comp) != len(second.comp):
            print("not the same dimenstion")
        return Vector(*(a - b for a, b in zip(self.comp, second.comp)))
    
    def __mul__(self, second):
        if isinstance(second, (int, float)):
            return Vector(*(a * second for a in self.comp))
        elif isinstance(second, Vector):
            if len(self.comp) != len(second.comp):
                print("not the same dimensions for dot product")
            return sum(a * b for a, b in zip(self.comp, second.comp))
        else:
            print("scalars or dot product with another vector")

    def __rmul__(self, second):
        return self * second  

    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.comp))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            print("cannot normalize a zero vector")
        return Vector(*(a / mag for a in self.comp))
    


# Example Usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)  # Output: Vector(1, 2, 3)

v3 = v1 + v2
print(v3)  # Output: Vector(5, 7, 9)

v4 = v2 - v1
print(v4)  # Output: Vector(3, 3, 3)

dot_product = v1 * v2
print(dot_product)  # Output: 32

v5 = 3 * v1
print(v5)  # Output: Vector(3, 6, 9)

print(v1.magnitude())  # Output: 3.7416573867739413

v_unit = v1.normalize()
print(v_unit)  # Output: Vector(0.2672612419124244, 0.5345224838248488, 0.8017837257372732)

