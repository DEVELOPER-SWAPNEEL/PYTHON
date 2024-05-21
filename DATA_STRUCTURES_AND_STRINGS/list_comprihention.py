'''x=[]
for i in range (11):
    z=i**2
    x.append(z)
print(x)'''
#------------>> TO WRITE THE SAME CODE IN MORE EFFICIENCY AND HAVING TIME AND SPACE COMPLEXITY..
lx=[i**2 for i in range(11)]
print(lx)
#---------->>>THE PROPER SYNTAX IS: list_name=[expression for items in list with loop upto range {if test expression}]
flag=[i**2 for i in range(11) if i**2 %2==0]
print("\n")
print(flag)