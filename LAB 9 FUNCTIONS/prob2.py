def repit(n):
    arr = []
    num = ''
    for i in range(0,n):
        num = num + f'{n}'
    num = int(num)
    arr.append(num)
   
    for i in range(1,n):
        num = num // 10
        arr.append(num)
       
    sum = 0
    for ele in arr:
        sum = sum + ele 
    return[print(sum , arr)]
repit(5)
    
    

    

            