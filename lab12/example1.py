import math
class Cylinder:
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius
    def get_height(self):
        return self.height
    def get_radius(self):
        return self.radius
    def set_height(self,height):
        self.height=height
    def set_radius(self,radius):
        self.radius=radius
    def base_area(self):
        return (math.pi*(self.radius**2))
    def surface_area(self):
        return 2*(math.pi)*(self.height)*self.radius
    def area(self):
        return 2*self.base_area()+self.surface_area()
    def volume(self):
        return self.base_area()*self.height

example=Cylinder(5,3)
print(example.volume())

