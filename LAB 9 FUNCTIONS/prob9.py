def count_alpha_digits(s):
    dic = { 'alpha' : 0 , 'digit' : 0 }
    for char in s:
        if char.isdigit():
            dic['digit'] += 1
        else:
            dic['alpha'] += 1
    return dic
s = input("enter any words and number: ")
print(count_alpha_digits(s))