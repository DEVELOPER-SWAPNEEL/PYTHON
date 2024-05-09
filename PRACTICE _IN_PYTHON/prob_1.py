#Given a list, write a Python program to swap first and last element of the list.

marks=[22,23,43,12]
last_element_index=len(marks)
flag=marks[0]
marks[0]=marks[last_element_index-1]
marks[last_element_index-1]=flag

print(marks)