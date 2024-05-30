def add(i,j):
    return i+j
# result= add(1,5)
# print(result)
# print(add(1,5))
a=add
print(a(1,5))
'''WE CAN ALSO CALL OTHER FUNCTION WITHIN THE ARGUMENTS OF A FUNCTION FOR eg:-  '''
def multi(k,add):
    return (k*add(5,5))
print(multi(5,add))