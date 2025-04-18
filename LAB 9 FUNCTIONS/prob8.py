def convert(l):
    l_0 = []
    words = l.split()
    new = sorted(set(words))
    new = " ".join(new)
    l_0.append(new)
    return l_0

l = input("enter your string to insert in list")
output = convert(l)
print(output)