#COLLECTION OF DATA
#WITHIN PARENTHESIS DATA IS PROVIDED
touple=(1,2,3,4,5,6)
print(touple)
print(touple[3])
toup_1=('niku',10,5.4)
toup_2=('swap',99)
final_toup=toup_1+toup_2
print(final_toup)#------------>>CONCARDINATION OF TWO TOUPLES
print(len(final_toup))
#------------->>>>>>>>>>>>VERY IMOPRTANT<<<<<<<<-----TOUPLES ARE IMMUTABLE---------->>>>>>>>>>>>>>
# touple[1]=98
# print(touple)
new_tup=(231,32545,6554,765,32,21,3,56,77,8,2,0,323,564,87)
sort_tup=sorted(new_tup)
print("THE NEW SORTED TOUPLE IS AS FOLLOWING:  ")
print(sort_tup)
print(sort_tup.index(6554))
