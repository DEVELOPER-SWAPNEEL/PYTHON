'''Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336'''
def multi(arr):
    result=1
    for i in arr:
        result*=i
    return result

list_input=input("ENTER THE ELEMENTS OF YOUR LIST SEPERATED BY SPACES : ")
num_list=[int(num) for num in list_input.split()]
result = multi(num_list)
print("THE MULTIPLICATIONS OF ALL THE ELEMENTS IN THE LIST IS : "+ str(result) )



