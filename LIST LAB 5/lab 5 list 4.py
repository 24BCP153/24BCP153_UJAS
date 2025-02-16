import random
number = [ random.randint(-30,30) for i in range(50)]
p_l = [  ]
n_l = [  ]
for i in number:
    if i>0:
        p_l.append(i)
    elif i<0:
        n_l.append(i)
print(p_l)        
print(n_l)
