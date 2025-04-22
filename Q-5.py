class Time:
    def add_times(self,h1,m1,s1,h2,m2,s2):
        h1 = h1*60*60
        m1 = m1*60
        total_in_sec = h1+m1+s1
        time1 = total_in_sec/3600
        h2 = h2*60*60
        m2 = m2*60
        total_in_sec2 = h2+m2+s2
        time2 = total_in_sec2/3600
        return time1+time2
    def sub_times(self,h1,m1,s1,h2,m2,s2):
        h1 = h1*60*60
        m1 = m1*60
        total_in_sec = h1+m1+s1
        time1 = total_in_sec/3600
        h2 = h2*60*60
        m2 = m2*60
        total_in_sec2 = h2+m2+s2
        time2 = total_in_sec2/3600
        if time1 > time2:
            return time1-time2
        elif time2 > time1:
            return time2 - time1
    
h1 = 4 
m1 =2 
s1 =24
h2 = 1 
m2 =0 
s2 = 23
operations = Time()
addition =  operations.add_times(h1,m1,s1,h2,m2,s2)
print(f"Addition of times is {addition} hours")

subtraction = operations.sub_times(h1,m1,s1,h2,m2,s2)
print(f"Subtraction of times is {subtraction} hours")

#OUTPUT:
# Addition of times is 5.046388888888889 hours
# Subtraction of times is 3.033611111111111 hours

