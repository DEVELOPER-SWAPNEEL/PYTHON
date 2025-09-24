f=float(input("\nENTRE THE TEMPRATURE IN F :"))
flag_1=input("DO YOU WANT TO CONVERT :  YES OR NO   :   ")
if(flag_1.lower() =='yes'):
    c=(f-32)*5/9
    print("THE TEMP IN CELCIUS IS FOUND TO BE: "+str(c)+" degree CELCIUS ")

