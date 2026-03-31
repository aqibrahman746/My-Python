""" <---- Multi-line comments and strings use this
Output
-------------------
#print("Hello World!", end=" ") #end= prints the next line on the same line
#print("Same line!")
#print("I am", 25)

# This is a comment

#print("This should not run")


This is 
a multiline
comment
"""

"""
Variables
-------------------
#x = "Khadija"
#y = 11
#print(x, y)
#print(type(x), type(y))
x, y, z = 'Me', 'You', 'I' #assigns multiple values to multiple variables
print(x, y, z)
x = y = z = "Abi" #assignsd one value to multiple variables
print(x, y, z)
"""

"""
Strings
#-------------------
a = "Hello World"
print(a[0]) #Select a character from string
#for x in "orange": #loop all characters
    #print(x)
print(len(a)) #number of characters
#print("World" in a) #check if string is inside
#print("Goodbye" not in a) #check if string is NOT inside
print(a[2:7]) #Characters from first index to second index
print(a[:4]) #From beginning
print(a[3:]) #To end
print(a[-5:-2]) #From first index up to, but not including, second index
print(a.upper()) #Uppercase all
print(a.lower()) #Lowercase all
print(a.replace("H", "Y")) #Replace string with another string
print(a.split(" ")) #Split the string where the separator is
b = 10
txt_1 = f"He is {b} now" #formats string
print(txt_1)
txt_2 = f"He will be {b * 2} soon" #has math capabilities
print(txt_2)
txt = "Hello, World!"
print(txt[2:5])
print(txt.upper())
name = "Python"
name = f"I love {name}"
print(name)

Operators
----------------------
#x = 18
#print(x / 3) #Returns float
#print(x // 3) #Floor division. Returns integer
#print(x % 4) #Modulus. Returns remainder

#x = 7
#x += 7 # x arithmeticOperator= num is the same as x = x arithmeticOperator num. So x += 7 is the same as x = x + 7
#print(x)

& = AND
| = OR
^ = XOR
~ = NOT
>> = right shift
<< = left shift

print(3 & 6) #Prints 2
print(6 | 8) #Prints 14
print(24 >> 2) #Prints 6
print(30 << 3) #Prints 240
"""