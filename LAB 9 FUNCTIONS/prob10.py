def frequency(s):
    s = s.split()
    frequency_new = {}

    for ele in s:
        if ele:
            frequency_new[ele] = frequency_new.get(ele,0) + 1
    return dict(sorted(frequency_new.items()))
s = input("enter your string:  ")
print(frequency(s))