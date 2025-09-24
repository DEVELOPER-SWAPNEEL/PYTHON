#USING PYTHON CODE AGE VOATING SEQUENCE 

age=input("\n\nENTRE YOUR AGE :-  ")
age_int=int(age)
if(age_int>=18):
    print("\nYOU CAN VOTE")
    print("\nYOU ARE AN ADULT")
elif(int(age)<18 and int(age)>=3):
    print("\nYOU ARE IN SCHOOL THE TEEN AGE PHASE")
else:
    print("\nYOU ARE A KID ")

print("\nTHANK YOU FOR YOU COOAPRATION")
