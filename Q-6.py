class Calendar:
    def __init__(self,lst):
        self.d = lst[0]
        self.m = lst[1]
        self.y = lst[2]

    def showdate(self):
        print(self.d,'/',self.m,'/',self.y)

    def __eq__(self,lst2):
        return (self.d == lst2.d) and (self.m == lst2.m) and (self.y == lst2.y)
    
lst1 = [23,5,2024]
lst2 = [21,6,2022]
date1 = Calendar(lst1)
date2 = Calendar(lst2)
date1.showdate()
date2.showdate()      

answer = date1 == date2       
print(answer)

#OUTPUT:
# 23 / 5 / 2024
# 21 / 6 / 2022
# False
