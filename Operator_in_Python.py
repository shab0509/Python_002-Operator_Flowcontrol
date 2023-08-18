#Operators in Python <BARLA|IM>
##################################################################

# 1__Arithmetic Operator
#################################

+ : Addition
- : Subtraction
* : Multiplication
/ : Division
% : Modulus
** : Exponential
// : Floor Division

a=float(input(print("Enter an number : ")))
b=float(input(print("Enter second number : ")))

print("_" * 50)
print("Arithmetic Operations")
print("_" * 50)

print("Sum of {},{} is {}".format(a,b,a+b))
print("Sub of {},{} is {}".format(a,b,a-b))
print("Mul of {},{} is {}".format(a,b,a*b))
print("Divison of {},{} is {}".format(a,b,a/b))
print("Floor Divison of {},{} is {}".format(a,b,a//b))
print("Modulus of {},{} is {}".format(a,b,a%b))
print("Exponential of {},{} is {}".format(a,b,a**b))

# 2__Assignment Operator
#################################

>>> Single Value Assignment
a=10
b=20
c = a+b
print(c)

>>>  Multi Valued Assignemnt
a,b,c= 10,20,30
ad,sb,mp = a+b, a-b,a*b*c
print(ad,sb,mp)
a=1000
b=1111
print(a,b)
a,b=b,a  #Swapping Logic
print(a,b)

# 3__Relational Operator
############################

> / < / >= / <= / == / !=

# 4__Bitwise Operator
#################################
>> Shift Operator
    1. Bitwise Left Shift Operator (<<)
    2. Bitwise Right Shift Operator (>>)

3. Bitwise OR (|)
4. Bitwise AND (&)
5. Bitwise NOT (~)
6. Bitwise XOR (^) <one value has 1 and other has to be 0>

# 5__ Membership Operator
######################################
# 2 types of operator
#   a> in
#   b> not in

l1= [10,'Rossum','Python',23.33,True]
print(l1)
print('Rossum' in l1)
print("shabi" not in l1)

s = "PYTHON"
print(s)

print('S' in s)
print('P' in s)

# 6__Identity Operator
############################
# returns true if var1 and var2 points different memory address otherwise false
# 2 types of identity operator :
#a> is
#b> is not

a= None
b= None
print(a,type(a),id(a))
print(b,type(b),id(b))
print(a is b)
print(a is not b)


s1=[10,20,30]
s2=[10,20,30]

print(s1,type(s1),id(s1))
print(s2,type(s2),id(s2))

print(s1 is s2)
print(s1 is not s2)



