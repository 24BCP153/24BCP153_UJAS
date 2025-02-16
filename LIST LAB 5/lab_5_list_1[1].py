import random
l = []
#n = int(input("enter a number that you get in list"))
for i in range(0,6):
    m = random.randint(1,101)
    if m%2 == 0:
        l.append(m)
   
print(l)

l_0 = []
#n = int(input("enter a number that you get in list"))
for i in range(0,5):
    m1 = random.randint(1,101)
    if m1%2 != 0:
        l_0.append(m1)
   
print(l_0)



