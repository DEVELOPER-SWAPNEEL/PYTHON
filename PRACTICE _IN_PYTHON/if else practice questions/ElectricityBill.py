'''Write a program to calculate the electricity bill (accept number of unit from user) according to
the following criteria :
Unit
First 100 units
Next 100 units
After 200 units
(For example if input unit is 350 than total bill amount is Rs2000)

Price
no charge
Rs 5 per unit
Rs 10 per unit'''

unit=int(input("\nENTRE THE NUMBER OF UNITS CONSUMED:-     "))
amt=0;
if(unit<100):
    print("\nTHE ENTRED UNIT IS BELOW CHARGEBLE LIMIT IT IS FREE!!!!")
elif(unit-100<100 and unit-100>0):
    amt=(unit-100)*5
elif(unit>200):
    amt=500+(unit-200)*10
print("\nTHE COST OF ELECTRICITY CONSUMED IS ₹",amt)
 


