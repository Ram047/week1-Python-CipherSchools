a=5+5
b=10-5
c=10/3 #it treats this as float (in case of float)
#in py3 it is treated float as number type int
#Floor Division
d=10//3 #now it does not belong to float type
isinstance(10.0,int) #integer and float are two diffent things
m=10%3 #gives the remainder
e=2**3 #(exponentiation)to raise to the power
str1='hello' + 'world'
mul='abc'*6
#Comparision operators
q=1==2
w=1 !=2
r=1<2
e=2>3
z="ab" < "z" #(due to lexigographical way)
s="a" <"A"
#  Logical Operators
a=True and False
b=True and False
c=True and 1
d= 1 and 0
e=1 and 5 
isinstance(True,int)
type(True)

#Short Circuiting:
type(True)
'''a or true = true
a or false = a
a and true =a
a and false = false'''
#you can solve bool operant with using only one operant
'''true or b=b(if b is truthy)
false or b=a(if a is falsy)
true and b=a(if b is truthy)
false and b=b (if b is falsy)'''
a="hello" and 6
a="" and 6 # output=""
b="" or 1.6 #output=1.6
a=bool("")
a=bool([1,2,3])
a=112 and 0
