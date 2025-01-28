l = [ 10 , 100 , 1000 ]
key = int(input("enter key that you want to search in list"))
for ele in l:
   if(key == ele):
      print(key,"is present in list")
      break
else:
    print(key,"is not present")
