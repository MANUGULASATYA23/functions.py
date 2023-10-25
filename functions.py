"""#String Transform Functions

#capitalize
#Syntax:variable.capitalize()

name="satya"
print(name.capitalize())

#Title
#syntax:variable.title()

name="satya swamy"
print(name.title())

#upper
#syntax:variable.upper()

name="amma"
print(name.upper())

#lower
#syntax:variable.lower()

name="SATYA"
print(name.lower())

#casefold
#syntax:variable.casefold()

name="SATYA"
print(name.casefold())

#swapcase
#syntax:variable.swapcase()

name="satya"
print(name.swapcase())


#String Check Functions

#isnumeric
#syntax:variable.isnumeric()
number="568"
print(number.isnumeric())

#isalphanumeric
#syntax:variable.ialnum()

num="satya123"
print(num.isalnum())

#isdecimal
#syntax:variable.isdecimal()

num="SATYA"
print(num.isdecimal())

#isdigit
#syntax:variable.isdigit()

num="7847"
print(num.isdigit())

#isascii
#syntax:variable.isascii()

num="abcde"
print(num.isascii())

#isupper
#syntax:variable.isupper()

num="satya"
print(num.isupper())

#islower
#syntax:variable.islower()

num="SATYA"
print(num.islower())

#isspace
#syntax:variable.isspace()

num=" "
print(num.isspace())

#isidentifier
#syntax:variable.isidentifier()

num="satya1234"
print(num.isidentifier())

#isprintable
#syntax:variable.isprintable()

num="satya@123"
print(num.isprintable())

#istitle
#syntax:variable.istitle()

num="satya swamy"
print(num.istitle())


#String Search Functions

#index
#syntax:variableName.index(string/char)

email="satya@gmail.com"
print(email.index("@"))
print(email.index(".com"))

email="satya"
print(email.index("@"))
print(email.index(".com"))



#rindex
#syntax:variableName.rindex(string/char)

email="satya@swamy@gmail.com"
print(email.rindex("@"))

#rfind
#syntax:variableName.rfind(string/char)

email="satya"
print(email.rindex("@"))

email="satya@gmail.com"
print(email.rindex("@"))
print(email.rindex(".com"))



#startswith
#syntax:variableName.startswith(string/char)

name="Satya@gmail.com"
print(name.startswith("Satya"))

#endswith
#syntax:variableName.endswith(string/char)

name="Satya@gmail.com"
print(name.endswith("Satya"))


#list methods

#Append
#syntax:lst.append(item)

lst=[]
lst.append("satya")
print(lst)

#insert
#syntax:lst.insert(index,item)

lst=["gowri","satya"]
lst.insert(1,"amani")
print(lst)

#Extend
#syntax:lst.extend(lst1)

a=["satya","sai"]
a1=["swamy","salmon"]
a.extend(a1)
print(a)

#count
#syntax:lst.count(item)

name=["satya","swamy"]
print(name.count("satya"))


#pop
#syntax:lst.pop()

name=["satya","swamy"]
name.pop()
print(name)

#remove
#syntax:lst.remove()

a=["satya","swamy"]
a.remove("satya")
print(a)

#clear
#syntax:lst.clear()

a=["swamy","dady","amma"]
print(a.clear())
print(type(a))
print(a)

#sort
#syntax:lst.sort()

lst=[8,4,9,2,6,8]
lst.sort()
print(lst)

#reverse
#syntax:lst.reverse()

a=[1,5,9,5,7]
a.reverse()
print(a)


#Tuple Methods

#count
#syntax:tpl.count(item)

tpl=tuple((1,2,3,7))
print(tpl.count(1))

#index
#syntax:tpl.index(item)

tpl=tuple((1,2,3,1))
print(tpl.index(2))

#set methods

#add
#syntax:variable.add(item)

a={'a','b','c'}
a.add('d')
print(a)

#update
#syntax:variable.update(setvariable)

a={'a','b','c'}
b={'b','c','d'}
a.update(b)
print(a)

#remove
#syntax:variableName.remove(item)

a={'a','b','c'}
a.remove('b')
print(a)

#discard
#syntax:variableName.discard(item)

a={'a','b','c'}
a.discard('b')
print(a)

#pop
#syntax:variableName.pop()

a={'a','b','c'}
a.pop()
print(a)

#union
#syntax:variableName.union(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection(b))

#intersection update
#yntax:set1.intersection_update

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
#syntax:set1.isdisjoint(set2)

a={'a'}
b={'b'}
print(a.isdisjoint(b))

#difference
#syntax:set1.difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.difference(b))

#symmetric difference
#syntax:set1.symmetric difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference(b))

#symmetric difference update
#syntax:set1.symmetric difference update(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset
#syntax:set1.issubset(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.issubset(b))

a={'b'}
b={'b','c'}
print(a.issubset(b))


#issuperset
#syntax:set1.issuperset(set2)

a={'a','b','c'}
b={'c'}
print(a.issuperset(b))

a={'a','b','c'}
b={'b','c','d'}
print(a.issuperset(b))"""


#frozenset methods

#union
#syntax:variableName.union(variable)

a=frozenset(('a','b','c'))
b=frozenset(('b','c','d'))
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)

a=frozenset(('a','b','c'))
b=frozenset(('b','c','d'))
print(a.intersection(b))


#isdisjoint
#syntax:set1.isdisjoint(set2)

a=frozenset(('a'))
b=frozenset(('b'))
print(a.isdisjoint(b))

#difference
#syntax:set1.difference(set2)

a=frozenset(('a','b','c'))
b=frozenset(('b','c','d'))
print(a.difference(b))

#symmetric difference
#syntax:set1.symmetric difference(set2)

a=frozenset(('a','b','c'))
b=frozenset(('b','c','d'))
print(a.symmetric_difference(b))

#issubset
#syntax:set1.issubset(set2)

a=frozenset(('a','b','c'))
b=frozenset(('b','c','d'))
print(a.issubset(b))

a=frozenset(('b'))
b=frozenset(('b','c'))
print(a.issubset(b))


#issuperset
#syntax:set1.issuperset(set2)

a=frozenset(('a','b','c'))
b=frozenset(('c'))
print(a.issuperset(b))

a=frozenset(('a','b','c'))
b=frozenset(('b','c','d'))
print(a.issuperset(b))

#copy
#syntax:set1.copy(set2)
a=frozenset(('a','b','c'))
b=frozenset(('c','d','e'))
c=a.copy()
print(c)
c=b.copy()
print(c)
