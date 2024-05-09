x=int(input("\nENTRE THE VALUE OF X:  "))
match x:
    case 0:
        print("\nTHE ENTRED CASE IS ZERO")
    case 4:
        print("\nTHE ENTRED CASE IS FOURE")
    case _ if x!=8:
        print("IT IS NOT 8 BUT:",x)
    case _ if x!=90:
        print("IT IS NOT 90 BUT:",x)