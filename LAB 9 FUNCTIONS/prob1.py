def count_low_up(s):
    dic = {'uppercase' : 0 , 'lowercase' : 0}
    for char in s:
        if char.islower():
            dic['lowercase'] += 1
        elif char.isupper():
            dic['uppercase'] += 1
    return dic
s = 'HELLo i am ujAs'
print(count_low_up(s))

