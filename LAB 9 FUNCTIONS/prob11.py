def create_list(l_1,l_2):
    result = list( set(l_1) & set(l_2))
    return result
l_1 = input("enter the first string:  ")
l_2 = input("enter the second string:  ")
print(create_list(l_1,l_2))