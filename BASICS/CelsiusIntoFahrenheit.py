c = int(input("ENTER THE TEMP IN CELSIUS: "))

flag_1 = input("\nDO YOU WANT TO CONVERT THE PARTICULAR TEMP INTO FAHRENHEIT: YES OR NO? ")

if flag_1.lower() == 'yes':
    f = (c * (9/5)) + 32
    print("TEMP IN FAHRENHEIT IS: " + str(f) + "°F")
