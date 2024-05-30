def max(a,b,c):
    if a >= b and a >= c:
        print("THE MAX OF ALL THREE IS: " + str(a))
    elif b >= a and b >= c:
        print("THE MAX OF ALL THREE IS: " + str(b))
    else:
        print("THE MAX OF ALL THREE IS: " + str(c))
num_1=int(input("ENTRE THE FIRST NUMBER: "))
num_2=int(input("ENTRE THE SECOEND NUMBER: "))
num_3=int(input("ENTRE THE THIRD NUMBER: "))
max(num_1,num_2,num_3)
