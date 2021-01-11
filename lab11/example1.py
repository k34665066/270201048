class cylinder:

    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def base_area(self):
        return 3.141592653589793*(self.radius**2)
    def surface_area(self):
        return 2*3.141592653589793*self.radius*self.height
    def volume(self):
        return self.base_area()*self.height
cylinder1=cylinder(3,5)
print(cylinder1.volume())
