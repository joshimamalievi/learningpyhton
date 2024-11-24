packing = [33, "yasim var dil vururam"]

global x, y 
x, y = packing

def myfunc():
 packing = [33, "vurmuram(good ending)"]
 global x, y 
 x, y = packing#changed it later overwriting it
 print(x, y)

myfunc()
print(x, y)

#this a comment mf