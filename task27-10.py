#parameter less
def add():
    a=10
    b=20
    print(a+b)
add()

#parameterized function
def add(literal1:int,literal2:int):
    print(literal1+literal2)
add(10,20)

#defined params
def add(literal1:int,literal2:int):
    print(literal1+literal2)
add(2,20)

#named params
def sub(literal1:int,literal2:int):
    print(literal1-literal2)
add(10, 20)
a=10
b=20
sub(literal1=a, literal2=b)
sub(literal2=b, literal1=a)

#optional params
def add(literal1:int,literal2:int,literal3=0):
    print(literal1+literal2+literal3)
add(2,20)
add(2,20,30)

#arbitary params
def add_arb(*literals):
    res: int=0
    for item in literals:
       res += item
       print(res)
add_arb(1, 2, 3, 4,5,6,7)

#arbitary key params
def userdetails(**literals):
    name=literals.get("name")
    email=literals.get("email")
    gender=literals.get("gender")
    print(name,email,gender)
userdetails(name="satya",email="s@gmail.com")

#returnable function
def add(literal1:int,literal2:int,literal3=0):
    return literal1+literal2+literal3
result=add(2,20,30)
print(result)


