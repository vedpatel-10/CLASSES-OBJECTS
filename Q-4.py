class ShapeInfo:
    def circumference(self,r):
        return (2*r*22)/7
    def area(self,r):
        return(r*r*22)/7
    
r = int(input("Enter the radius of circle :"))
values = ShapeInfo() 
circ = values.circumference(r)
area = values.area(r)

print("The area of circle is :"+str(area))
print("The circumference of circle is : "+str(circ))

#OUTPUT:
# Enter the radius of circle :7
# The area of circle is :154.0
# The circumference of circle is : 44.0
