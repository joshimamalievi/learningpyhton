b = "Hello, World"
print(b[2:5]) # this returns characters between the position given
print(b[:5]) # this returns from the beginning character to the given position
print(b[2:]) # and this is the other way around
print(b[-5:-2]) # this starts from the other side of the String

print("--------------------------------Modifying the string---------------------------------------")

print(b.upper()) # upper case
print(b.lower()) # lower case
print(b.strip()) # strips the whitespace around the string not inside if " HELLO WORLD " then returns "HELLO WORLD"
print(b.replace("H", "J")) # replaces the given char with the other string given
print(b.split(",")) # splits from the given char or string


print("---------------------------------CONCAT STRING---------------------------------------------")
x = "Vusal"
y = "Joshgun"
z = x + " " + y

print(z)
print("--------------------------------FORMATTTING------------------------------------------------")

a = 33
c = f"{a} yasim var" # in order to concat integer and a string together we use 'f"{var} String"'
print(c)

# we can also modify the int this way:

d = f"{a:.2f} manata verirem" # this will make it seem like the int is actually a float outputting '33.00'
print(d)
# You can also perform math if its done in '{}' semicolons
print(f"{33*25:.2f} manata cixiram. Beli, men valikem")