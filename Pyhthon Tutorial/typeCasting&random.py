import random;

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
print(" --------------------------- -------------------------- ------------------------- ---------------------- ")
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

print("++++++++++++++++++++++++++++++++++++++++++++++++TYPE CASTING++++++++++++++++++++++++++++++++++++++++++++++")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("______________________________________________RANDOM NUMBER_____________________________________________")


print("\n", random.randrange(1,10))