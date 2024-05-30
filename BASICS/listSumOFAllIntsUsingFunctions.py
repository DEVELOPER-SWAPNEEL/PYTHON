''' Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''
def sum(listtt):
    sum=0
    for i in listtt:
        sum+=i
        i=i+1
    return sum

input_1=input("ENTRE THE ELEMENTS OF THE LIST WITH SPACES PRESENT ")

list_1= [int(num) for num in input_1.split()]
print(list_1)

print("THE SUM OF ALL THE ELEMENTS PRESENT IN THE LIST IS:  "+str(sum(list_1)))

