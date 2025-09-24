class const_dect:
    x=0
    def __init__(self,clr,typ):
        self.clr=clr
        self.typ=typ
        print("constructed".upper())
    # def __del__(self):
    # print("destructors".upper())
    
cd=const_dect("Black".capitalize(),"suv".upper())
print(cd.clr)
print(cd.typ)
cd_1=const_dect("red".capitalize(),"sudan".capitalize())
print(cd_1.clr)
print(cd_1.typ)
