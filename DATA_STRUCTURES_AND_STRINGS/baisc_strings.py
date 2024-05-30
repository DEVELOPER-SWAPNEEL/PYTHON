name= 'swapneel purohit'
print(name.capitalize())       #FIRST LETTER CAPITAL OF FIRST WORD
print(name.upper())
print(name.lower())
#------------------------------------------------------------------------------------------------------------
a='7'
print(a.isnumeric())
# an=7
# print(an.isnumeric())  ERROR WILL COME IF YOU WANT TO VERIFY PRE MADE INTEGER IT IS ONLY POSSIBLE FOR STRINGS
print(a.isalpha())
k='   niku is a good boy'
print(k.startswith('niku'))
print(k.endswith('bot'))
print(k.replace('niku','neha'))
print(k.find('a'))
print(k)
print(k.lstrip())
nk='baby see me hu south delhi kii     '
print(nk.rstrip())#REMOVES SPACES AT THE RIGHT EXTREAM
print(nk.split())#-----IT WILL SPLIT THE WHOLE STRING INTO A LIST WITH EACH WORD AS ELEMENT
print(nk.splitlines())
kiwi='niku','neha'
print(kiwi)
comma=','
print(comma.join(kiwi))
