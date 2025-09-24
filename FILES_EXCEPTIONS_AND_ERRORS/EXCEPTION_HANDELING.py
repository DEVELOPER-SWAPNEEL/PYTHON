'''
a=2
b=0
------>this will give an error but to avoid the pop-up red error and consider it as "hit and try method"then we use:
'''
try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError:
    print("THERE IS AN ERROR")
finally:
    print("CONTINUE WITH THE FOLLOWING CODE")