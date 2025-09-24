lx=['neha', 'niku', 'miki', 'zig', 10, 2, 9.5]
lx.pop(2)
print(lx)
lx.insert(1,'hkp')
print(lx)
#----------THE DIFFERENCE IN APPEND ,EXTEND WITH INSERT THAT IN THE APPEND OR EXTEND WE CAN ADD VALUES TO THE END OF THE LIST BUT 
#----------BUT IN INSERT FUNCTION WE CAN ADD ANY STRING TO THE LIST IN ANY INDEX;
lx[0:3]=[345,645,23,43]
print(lx)
lx.remove('zig')
print(lx)
lx.sort()   #----------THIS FUNCTION ARRANGES THE LIST IN ASSENDING ORDER   {ONLY IF PRESENT IN INT FORM COMBINATION OF STR AND INT WILL GIVE ERROR}
print(lx)
lx.reverse() #----------THIS FUNCTION ARRANGES THE LIST IN DESENDING ORDER 
print(lx)
print(lx.index(10))
