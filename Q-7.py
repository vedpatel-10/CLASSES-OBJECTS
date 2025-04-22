class Weather:
    def __init__(self,lst):
        self.type = lst[0]
        self.pressure = lst[1]
        self.temperature = lst[2]
    def __contains__(self,data):
        return data in [self.type,self.pressure,self.temperature]

lst = ["sunny",'1pascal','31 deg. celsius']
parameters = Weather(lst)
data = (input("Enter a parameter : "))

answer = data in parameters
print(answer)

#OUTPUT:
# Enter a parameter : 1pascal
# True
