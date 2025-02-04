def vowels(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u' :
            count = count+1
    print(count)
a = input("enter the string")
vowels(a)
