def factorial(n):
    if(n<2):
        return 1
    else:
        return n*(factorial(n-1))
num= int(input("ENTRE THE NUMBER FOR FACTORIAL: "))
print("THE FACTORIAL OF THE PROVIDED NUMBER IS FOUND TO BE : "+str(factorial(num)))