#DATA PRINTING IN PYTHON
######################################
#Syntax_001:
a=10
print(a)
print("_"*40)

#Syntax_002:
print("Hello Python")
print("Hello " + "Python " + "World")
print("_"*40)

#Syntax_003:
b=20
print("val of a:",b)
print("_"*40)

#Syntax_004:
c=21
d=31
sum=c+d
print("val of a:",c,"and",d,"is",sum )
print("_"*40)

#Syntax_005:<print(value cum message with format)>
x=10
y=11
total = x+y
print("value of x:{} ".format(x))
print("value of y:{} ".format(y))
print("Sum total of {} and {} is {}".format(x,y,total))
print("_"*40)

#Syntax_005:<print(value cum message with format specifier)>
m=45
print("Value of m=%d" %m,type(m))
print("Value of m=%f" %m,type(m))
print("Value of m=%.2f" %m,type(m))
print("Value of m=%s" %m,type(m))
p,q,r=15,20,35
print("sum of %d and %d is %f"%(p,q,r))
print("_"*40)