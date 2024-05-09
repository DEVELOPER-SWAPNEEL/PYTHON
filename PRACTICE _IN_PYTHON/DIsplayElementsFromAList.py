# Display numbers from a list using loop
# Taking space-separated input for a list of integers using list comprehension
input_list = [int(num) for num in input("Enter space-separated integers: ").split()]
print("Input list:", input_list)
print(type(input_list))
for element in input_list:
    if(element>150):
        print(element,"continue is applied element being more the 150")
        continue
    elif(element>500):
        break
        print("loop ended")
    elif(element%5==0):
        print("\nNUMBERS DIVISIBLE BY 5:    ",element)
    elif(element%5!=0):
        print("\nNUMBER IS NOT DIVISIBLE BY 5:    ",element)# input_list=(input("\nENTRE THE SPACED STRING TO BE CONVERTED INTO A LIST:    ").split())
# for i in input_list:
#   input_list_num=int(i)
# print(input_list_num)
# type(input_list_num)