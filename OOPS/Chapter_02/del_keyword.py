class Students:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

s1 = Students("ABC", 55)
print(s1.name)
print(s1.mark)

del s1.mark         # delete mark properties
print(s1.mark)      # output => 'Students' object has no attribute 'mark'