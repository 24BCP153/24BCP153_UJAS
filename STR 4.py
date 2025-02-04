def remove(s1, s2):
    result = ""  
    i = 0 

    while i < len(s1):
        
        if s1[i:i+len(s2)] == s2:
            i += len(s2)
        else:
            result += s1[i]
            i += 1

    return result


s1 = input("Enter the main string: ")
s2 = input("Enter the string to remove: ")
print(remove(s1, s2))

