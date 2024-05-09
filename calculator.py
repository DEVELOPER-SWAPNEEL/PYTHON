flag_1=input("\n\nENTRE THE FIRST NUMBER ")
flag_2=input("\n\nENTRE THE SECOND NUMBER ")
num1=int(flag_1)
num2=int(flag_2)

flag_3= input("\nENTRE THE KIND OF OPERATION TO BE PERFORMED  FORM THE LIST BELOW \n1.SUM  \n2.SUBSTRACT   \n3.MULTIPLICATION  \n4.DIVIDE:-  ")  

opt =int(flag_3)
if (opt == 1):
    print("\n THE SUM OF THE TWO NUMBERS ARE:-   ",num1 + num2)
elif(opt == 2):
    print(num1-num2)
elif(opt == 3):
    print(num1*num2)
elif(opt == 4):
    print(num1/num2)

else:
    print("\nTHE ENTRED OPTION IS EITHER WRONG OR SPELLING IS NOT CORRECT   ")

