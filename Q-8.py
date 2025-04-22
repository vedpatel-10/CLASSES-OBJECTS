class String:
    def __init__(self,str):
        self.str = str
    def toLower(self):
        a = self.str.lower()
        return a
    def toUpper(self):
        b = self.str.upper()
        return b
    def __iadd__(self, other):
        return self.str + other.str
   
        
str1 = "Hello"
str2 = "world"
str_obj1  = String(str1)
str_obj2 = String(str2)
answer1 = str_obj1.toLower()
print(answer1)
answer2 = str_obj2.toUpper()
print(answer2)

str_obj1 += str_obj2
print(str_obj1)

#OUTPUT:
# hello
# WORLD
# Helloworld

