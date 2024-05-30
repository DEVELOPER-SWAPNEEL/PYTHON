# IT IS A TYPE OF COLLECTION
# IT IS UNORDERED WHICH MEANS IT DOESNOT POSSESS ANY INDEX
# IT IS UNIQUE :- ONE SET DOESNOT REPEATE ITS ELEMENTS..
# THE SETS ARE REPRESENTED WITHIN {}
sets={1,2,3,4,5,12}
print(sets)
sets.add(6)
print(sets)
sets.remove(2)
print(sets)
print(6 in sets)
print(0 in sets)
set_1={1,2,3,4,5,6,7,8}
print(sets & set_1)
print(sets.union(set_1))

set_3={1,2,3,4,5,6,7,8,9,10}
set_4={1,2,3,4,5}
print(set_4.issubset(set_3))