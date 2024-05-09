# i=int(input("\nENTRE THE NO. OF ROWS YOU WANT TO PRINT:  "));
# for p in range(i):
#     for q in range(p):  print(q+1)
        
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row= int(input("\nENTRE THE NO.OF ROWS YOU WANT THE PATTERN:    "))
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")
