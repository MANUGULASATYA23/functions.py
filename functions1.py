#String Transform Functions

#capitalize
#Syntax:variable.capitalize()
def capitalize():
    name="satya"
    print(name.capitalize())
capitalize()

#Title
#syntax:variable.title()
def title():
    name="satya swamy"
    print(name.title())
title()

#upper
#syntax:variable.upper()
def upper():
    name="amma"
    print(name.upper())
upper()

#lower
#syntax:variable.lower()
def lower():
    name="SATYA"
    print(name.lower())
lower()

#casefold
#syntax:variable.casefold()
def casefold():
    name="SATYA"
    print(name.casefold())
casefold()

#swapcase
#syntax:variable.swapcase()
def swapecase():
    name="satya"
    print(name.swapcase())
swapecase()

#String Check Functions

#isnumeric
#syntax:variable.isnumeric()
def isnumeric():
    number="568"
    print(number.isnumeric())
isnumeric()

#isalphanumeric
#syntax:variable.ialnum()
def isalphanumeric():
    num="satya123"
    print(num.isalnum())
isalphanumeric()

#isdecimal
#syntax:variable.isdecimal()
def isdecimal():
    num="SATYA"
    print(num.isdecimal())
isdecimal()

#isdigit
#syntax:variable.isdigit()
def isdigit():
    num="7847"
    print(num.isdigit())
isdigit()

#isascii
#syntax:variable.isascii()
def isascii():
    num="abcde"
    print(num.isascii())
isascii()

#isupper
#syntax:variable.isupper()
def isupper():
    num="satya"
    print(num.isupper())
isupper()

#islower
#syntax:variable.islower()
def islower():
    num="SATYA"
    print(num.islower())
islower()

#isspace
#syntax:variable.isspace()
def isspace():
    num=" "
    print(num.isspace())
isspace()

#isidentifier
#syntax:variable.isidentifier()
def isidentifier():
    num="satya1234"
    print(num.isidentifier())
isidentifier()

#isprintable
#syntax:variable.isprintable()
def isprintable():
    num="satya@123"
    print(num.isprintable())
isprintable()

#istitle
#syntax:variable.istitle()
def istitle():
    num="satya swamy"
    print(num.istitle())
istitle()

#String Search Functions

#index
#syntax:variableName.index(string/char)
def index():
    email="satya@gmail.com"
    print(email.index("@"))
    print(email.index(".com"))
index()

#rindex
#syntax:variableName.rindex(string/char)
def rindex():
    email="satya@swamy@gmail.com"
    print(email.rindex("@"))
rindex()

#rfind
#syntax:variableName.rfind(string/char)
def rfind():
    email="satya@gmail.com"
    print(email.rindex("@"))
    print(email.rindex(".com"))
rfind()


#startswith
#syntax:variableName.startswith(string/char)
def startwith():
    name="Satya@gmail.com"
    print(name.startswith("Satya"))
startwith()

#endswith
#syntax:variableName.endswith(string/char)
def endswith():
    name="Satya@gmail.com"
    print(name.endswith(".com"))
endswith()

#list methods

#Append
#syntax:lst.append(item)
def append():
    lst=[]
    lst.append("satya")
    print(lst)
append()

#insert
#syntax:lst.insert(index,item)
def insert():
    lst=["gowri","satya"]
    lst.insert(1,"amani")
    print(lst)
insert()

#Extend
#syntax:lst.extend(lst1)
def extend():
    a=["satya","sai"]
    a1=["swamy","salmon"]
    a.extend(a1)
    print(a)
extend()

#count
#syntax:lst.count(item)
def count():
    name=["satya","swamy"]
    print(name.count("satya"))
count()

#pop
#syntax:lst.pop()
def pop():
    name=["satya","swamy"]
    name.pop()
    print(name)
pop()

#remove
#syntax:lst.remove()
def remove():
    a=["satya","swamy"]
    a.remove("satya")
    print(a)
remove()

#clear
#syntax:lst.clear()
def clear():
    a=["swamy","dady","amma"]
    print(a.clear())
    print(type(a))
    print(a)
clear()

#sort
#syntax:lst.sort()
def sort():
    lst=[8,4,9,2,6,8]
    lst.sort()
    print(lst)
sort()

#reverse
#syntax:lst.reverse()
def reverse():
    a=[1,5,9,5,7]
    a.reverse()
    print(a)
reverse()

#Tuple Methods

#count
#syntax:tpl.count(item)
def count():
    tpl=tuple((1,2,3,7))
    print(tpl.count(1))
count()

#index
#syntax:tpl.index(item)
def index():
    tpl=tuple((1,2,3,1))
    print(tpl.index(2))
index()

#set methods

#add
#syntax:variable.add(item)
def add():
    a={'a','b','c'}
    a.add('d')
    print(a)
add()

#update
#syntax:variable.update(setvariable)
def update():
    a={'a','b','c'}
    b={'b','c','d'}
    a.update(b)
    print(a)
update()

#remove
#syntax:variableName.remove(item)
def remove():
    a={'a','b','c'}
    a.remove('b')
    print(a)
remove()

#discard
#syntax:variableName.discard(item)
def discard():
    a={'a','b','c'}
    a.discard('b')
    print(a)
discard()

#pop
#syntax:variableName.pop()
def pop():
   a={'a','b','c'}
   a.pop()
   print(a)
pop()

#union
#syntax:variableName.union(variable)
def union():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.union(b))
union()

#intersection
#syntax:variableName.intersection(variable)
def intersection():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.intersection(b))
intersection()

#intersection_update
#yntax:set1.intersection_update
def intersection_update():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.intersection_update(b))
    print(a)
    print(b)
intersection_update()

#isdisjoint
#syntax:set1.isdisjoint(set2)
def isdisjoint():
    a={'a'}
    b={'b'}
    print(a.isdisjoint(b))
isdisjoint()

#difference
#syntax:set1.difference(set2)
def difference():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.difference(b))
difference()

#symmetric_difference
#syntax:set1.symmetric_difference(set2)
def symmetric_difference():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.symmetric_difference(b))
symmetric_difference()

#symmetric difference update
#syntax:set1.symmetric difference update(set2)
def symmetric_difference_update():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.symmetric_difference_update(b))
    print(a)
    print(b)
symmetric_difference_update()

#issubset
#syntax:set1.issubset(set2)
def issubset():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.issubset(b))
issubset()

def issubset():
    a={'b'}
    b={'b','c'}
    print(a.issubset(b))
issubset()

#issuperset
#syntax:set1.issuperset(set2)
def issuperset():
    a={'a','b','c'}
    b={'c'}
    print(a.issuperset(b))
issuperset()

def issuperset():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.issuperset(b))
issuperset()

#frozenset methods

#union
#syntax:variableName.union(variable)
def union():
    a=frozenset(('a','b','c'))
    b=frozenset(('b','c','d'))
    print(a.union(b))
union()

#intersection
#syntax:variableName.intersection(variable)
def intersection():
    a=frozenset(('a','b','c'))
    b=frozenset(('b','c','d'))
    print(a.intersection(b))
intersection()

#isdisjoint
#syntax:set1.isdisjoint(set2)
def isdisjoint():
    a=frozenset(('a'))
    b=frozenset(('b'))
    print(a.isdisjoint(b))
isdisjoint()

#difference
#syntax:set1.difference(set2)
def difference():
    a=frozenset(('a','b','c'))
    b=frozenset(('b','c','d'))
    print(a.difference(b))
difference()

#symmetric difference
#syntax:set1.symmetric difference(set2)
def symmetric_difference():
    a=frozenset(('a','b','c'))
    b=frozenset(('b','c','d'))
    print(a.symmetric_difference(b))
symmetric_difference()

#issubset
#syntax:set1.issubset(set2)
def issubset():
    a=frozenset(('a','b','c'))
    b=frozenset(('b','c','d'))
    print(a.issubset(b))
issubset()

def issubset():
    a=frozenset(('b'))
    b=frozenset(('b','c'))
    print(a.issubset(b))
issubset()

#issuperset
#syntax:set1.issuperset(set2)
def issuperset():
    a=frozenset(('a','b','c'))
    b=frozenset(('c'))
    print(a.issuperset(b))
issuperset()

def issuperset():
    a=frozenset(('a','b','c'))
    b=frozenset(('b','c','d'))
    print(a.issuperset(b))
issuperset()

#copy
#syntax:set1.copy(set2)
def copy():
    a=frozenset(('a','b','c'))
    b=frozenset(('c','d','e'))
    c=a.copy()
    print(c)
    c=b.copy()
    print(c)
copy()