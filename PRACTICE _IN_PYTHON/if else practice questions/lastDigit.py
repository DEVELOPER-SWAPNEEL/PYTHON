'''FIND THE LAST DIGIT OF A NUMBER'''
num=int(input("\nENTRE THE NUMBER:  "))
flag_1=num%10

if(flag_1%3==0):
    print("\nTHE ENTRED NUMBER IS DIVISIABLE BY 3")
else:
    print("\nENTRED NUMBER IS NOT DIVISIBLE BY 3")
