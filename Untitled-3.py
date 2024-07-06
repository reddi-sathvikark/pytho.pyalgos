def ispalindrome():
        x=121
        converted=str(x)
        xrev=converted[::-1]
        print(converted)
        print(xrev)
        if converted==xrev:
            print("x is a palindrome")
        else:
            print("x is not a palindrome")
            

ispalindrome()