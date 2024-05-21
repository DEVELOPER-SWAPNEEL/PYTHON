dictionary={'a':'apple','b':'boll','c':'cat','d':'dog'}
dictionary['e']='elephant'
del(dictionary['c'])
print(dictionary)
#TO CHECK WHEATHER A KEY IS PRESENT IN A DICTIONARY:
print('a'in dictionary)
print('g'in dictionary)
#TO PRINT ALL THE KERY PRESENT IN A DICTIONARY
print(dictionary.keys())
#values:
print(dictionary.values())
#TO CHECK WHEATHER A KEY IS PRESENT IN A DICTIONARY with a contomized message:::
print(dictionary.get('g',"g not present in the dictionary"))
