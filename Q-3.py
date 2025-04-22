class SolidInfo: 
    def surface_area(self,l,b,h):
        return (2*(l*b +b*h + h*l))
    def volume(self,l,b,h):
        return (l*b*h)
    
l = int(input("Enter length of Cuboid: "))
b = int(input("Enter breadth of Cuboid: "))
h = int(input("Enter height of Cuboid: "))

values = SolidInfo()
sa = values.surface_area(l,b,h)
v = values.volume(l,b,h)

print("The surface area of cuboid is : "+str(sa))
print("The volume of cuboid is : "+str(v))

#OUTPUT:
# Enter length of Cuboid: 6
# Enter breadth of Cuboid: 4
# Enter height of Cuboid: 25
# The surface area of cuboid is : 548
# The volume of cuboid is : 600

