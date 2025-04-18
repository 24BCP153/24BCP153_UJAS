def is_palindrome(a):

    reverse = 0
    origanal = a

    while a > 0:
        rmd = a % 10              # FOR REMAINDER (LAST DIGIT)
        reverse = reverse * 10 + rmd                   # not a bec orig is copy not chanfe in loop USE a only
        a = a // 10      # FOR REMOVE ONE DIGIT

    if origanal == reverse:
        print("Number is a palindrome!")
    else:
        print("Number is not a palindrome.")

num = int(input("your number for check palindrome num.. : "))
is_palindrome(num)