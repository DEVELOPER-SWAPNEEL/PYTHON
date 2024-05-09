row= int(input("\nENTRE THE NO.OF ROWS YOU WANT THE PATTERN:    "))

for i in range(1,row+1,1):
    for j in range(1,i+1):
        print("*",end=' ')
    print("")
