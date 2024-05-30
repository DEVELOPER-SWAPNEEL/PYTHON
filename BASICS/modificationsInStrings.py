#IMPORTANT!!!  PRINT STRINGS ARE IMMUTABLE HENCE IT WILL ONLY PRINT THE PARTICULAR OPERATION AND NOT CHANGE THE ORIGINAL STRING
sting= ("***SWapNeeL Purohit*******************")
print(sting)
print(sting.replace("Purohit","PUROHIT"))#FOR REPLACE 
print(sting.upper())#FOR UPPER CASE
print(sting.rstrip("*"))#THIS WILL REMOVE ALL THE CHARACTER PRESENT WITHIN THE INVERTED COMMAS
head=("welcome to my profile")
print(head.capitalize())#THIS WILL CAPITILIZE YOUR STRING ONLY FIRST LETTER THEN ALL SMALL  
print(head.split(" ")) #IT WILL SPLIT THE STRING INTO PARTICULAR LIST HAVING THE SPLIT JUNCTION AS MENTIONED WITHIN INVERTED COMMAS

print(len(head))#PRINT THE LENGTH OF THE STRING
print(head.center(50))#WILL CREATE MORE SPACE ENTRED THROUGH THE PARENTHESIS AND MAKE THE STRING INTO THE CENTRE
print(head.center(50,"!"))#print rest space as provided
print(len(head.center(50))) #ANS IS 50 SO AS ENTRED 
print(sting.count("Purohit"))#COUNT THE NO. OF WORDS ENTRED PRESENT IN THE STRING
print(sting.endswith("*"))#CHECK IT WILL END WITH THE ENTRED PART OR NOT 
print(head.endswith("to",1,10))#CHECKS THAT WHEATHER THE PROVIDED PART ENDS IN THE PROVIDED LENGTH THE LAST LIMIT IS DETERMINING STEP PREVIOUT OR STATING CAN BE MORE THEN THE STARTING OF THE WORD
print(head.find("to"))#print the FIRST LETTER'S index of the entred one's//not present then outpur is -1orFALSE
print(head.index("profile"))#same as above but difference is 
#print(head.index("nik"))#if not FOUND THEN IT WILL THROUGH ERROR
print(head.isalnum())#The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
#space is also considered as a character and takes index value also inalnum() will retuen false if space is present
print(head.isalpha())#The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(head.islower())#The islower() method returns True if all the characters in the string are lower case, else it returns False.
print(head.isprintable())#The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
print(head.isspace())#The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
print(head.istitle())#The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
flag2="HI MY NAME IS SWAPNEEL PUROHIT"
print(flag2.isupper())#The isupper() method returns True if all the characters in the string are upper case, else it returns False.
print(flag2.startswith("HI"))#The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
flag=flag2.swapcase()#The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
print(flag)
print(flag.title())#The title() method capitalizes each letter of the word within the string.

#replit link:-  "https://replit.com/@rsnikupurohit17/13-Day13-String-Methods"


