#A single line comment in python

''' A multiple 
line comment
in python'''

""" Another multiple 
line comment
in python"""

#Print Statement
#print('hello world') #outPut: hello world

#variable & datatypes
#variables don't need to be declared in python
'''
a = 5 #value assigning to variable and the variable datatype is integer
A = 7 #Case-Sensitive
b = 'John' #value assigning to variable and the variable datatype is string
c = '6' #value assigning to variable and the variable datatype is string
d = 4.6 #value assigning to variable and the variable datatype is float
e = True #value assigning to variable and the variable datatype is bool
f = g = h = 25 #the same value assigning to many variables
i = str(78)    
j = int(78)    
k = float(78)
x, y, z = "Orange", 5, 8.9

print(a) #outPut: 5
print(A) #outPut: 7
print(b) #outPut: John
print(c) #outPut: 6 (but it's string)
print(d) #outPut: 4.6
print(e) #outPut: true
print(f) #outPut: 25
print(g) #outPut: 25
print(h) #outPut: 25
print(i) #outPut: 78 (but it's string)
print(j) #outPut: 78
print(k) #outPut: 78.0
print(x) #outPut: orange
print(y) #outPut: 5
print(z) #outPut: 8.9

print(x,y,z) #outPut: orange 5 8.9
print(x+b) #outPut: orangeJohn

#we can check all the variable's data type with type function
print(type(a)) #outPut: <class 'int'>
print(type(A)) #outPut: <class 'int'>
print(type(b)) #outPut: <class 'str'>
print(type(c)) #outPut: <class 'str'>
print(type(d)) #outPut: <class 'float'>
print(type(e)) #outPut: <class 'bool'>
print(type(f)) #outPut: <class 'int'>
print(type(g)) #outPut: <class 'int'>
print(type(h)) #outPut: <class 'int'>
print(type(i)) #outPut: <class 'str'>
print(type(j)) #outPut: <class 'int'>
print(type(k)) #outPut: <class 'float'>
print(type(x)) #outPut: <class 'str'>
print(type(y)) #outPut: <class 'int'>
print(type(z)) #outPut: <class 'float'>
'''
#Legal variable names 
'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 
camelCaseVariableName = "John" 
PascalCaseVariableName = "John" 
snake_case_variable_name = "John" 
'''
#we also can assign value like this
'''
x = str("Hello World")	
x = int(20)	
x = float(20.5)	
'''
"""
x = 5
y = 3
#Arithmetic Operator
print(x + y) #output: 8
print(x - y) #output: 2
print(x * y) #output: 15
print(x / y) #output: 1.6666666666666667
print(x % y) #output: 2
print(x ** y) #output: 125
print(x // y) #output: 1

#Comparison
print(x == y) #output: False
print(x != y) #output: True
print(x < y) #output: False
print(x > y) #output: True
print(x <= y) #output: False
print(x >= y) #output: True

#Assignment operators
x += 20
print(x) #output: 25
x -= 2
print(x) #output: 23
x *= 2
print(x) #output: 46
x /= 2
print(x) #output: 23.0
x %= 3
print(x) #output: 2.0
x **= 2
print(x) #output: 4.0
x //= 2
print(x) #output: 2.0

#Logical operators
print(x>3 and x<10) #output: False
print(x>3 or x<10) #output: True
print (not(x>3 or x<10)) #output: False
print (not(x>3 and x<10)) #output: True

#Identity Operator
x = 7
y = 4
z = x
print(x is y) #output: False 
print(x is z) #output: True
print(x is not y) #output: True
print(x is not z) #output: False

#Membership Operator
x = ["apple", "banana"]
print("banana" in x) #output: True
print("cherry" in x) #output: False
print("banana" not in x) #output: False
print("cherry" not in x) #output: True
"""