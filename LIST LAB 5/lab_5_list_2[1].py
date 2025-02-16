import random
l = []
n = int(input("enter a number that you get in list"))
d = int(input("enter the numbr which you show that index of the "))
for i in range(0,n+1):
    m = random.randint(1,21)
    l.append(m)
    if m==d:
        g=l.index(d)    

print(l)
print(g)
