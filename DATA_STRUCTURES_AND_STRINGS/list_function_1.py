lx=['neha','niku','miki']
lx.append('zig')
print(lx)
lx.extend([10,2,9.5])
print(lx)
'''IN APPEND FUNCTION YOU CAN ADD ONLY A SINGLE VALUE TO THE LIST BUT IN EXTEND YOU CAN DO MULTIPLE INPUTS'''
lx.remove('miki')
print(lx)
del lx[3:6]
print(lx)
'''THE DIFFERENCE B/W lx.remove AND del lx[only index]or del lx[staring index : final index] in del function we can 
    DELETE MULTIPLE ELEMENTS IN THE LIST WITH PROVIDING INDEX.. BUT IN REMOVE WE CAN ONLY REMOVE A PERTICULAR ELEMENT IN THE LIST'''
#TO MAKE A LIST AS BLACK LIST WE USE
lx.clear()
print(lx)