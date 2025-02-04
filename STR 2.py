def own(s):
    s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s2="abcdefghijklmnopqrstuvwxyz"
    new = " "
    for i in range(len(s)):
        for j in range(len(s1)):
            if s[i] == s1[j]:
                new += s2[j]
                break
            else:
                new += s[i]
    print(new)
s = input("enter your string")
own(s)
