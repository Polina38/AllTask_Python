from re import X


x=0
y=0

def Saver(a,b):
    global x
    global y
    x,y=a,b
   

def Keeper():
    global x
    global y
    return x,y

