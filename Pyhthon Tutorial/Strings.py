#Strings

a = "Hello, World!"

print(a[1])#Getting the given position char

# looping through a String

for x in "banana":
 print(x)

print(len(a)) #length of the String

#Checking if if it exists

print("Hello" in a)# it will return a boolean value

# using 'if' function

if "Hello" in a:
 print("Yes 'Hello' exists in this String")

# checking if not

print("Hello" not in a)

# usin if

if "Hello" not in a:
 print("NO 'Hello' doesnt exist in this String")
else:
 print("Hello does exist in this String")