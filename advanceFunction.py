# def pranam():
#     print("namaste")
#
#
# pranam()
from functools import reduce

# def pranam(n="ram",age=25):
#     print(f'namaste {n} from {age} years future' )
#
# pranam("aam")
# pranam("as" ,34)


# def asd(*args):
#     print(args)
#
# asd("we",4,3,4,5)


# def asd(**s):
#     print(s)
#     for k, v in s.items():
#         print(k, v)
# asd(name="Prince",age=20)

# sq=lambda x:x/4
# print(sq(10))
# add=lambda x,y,z:x**x+y**z
# print(add(1,2,3))


# def avg(*n):
#     s=sum(n)
#     print(s/len(n))
#
# avg(1,2,3,4,5)

# even=lambda x: "even " if x%2==0 else "odd"
# print(even(3))
#
# def details(**fields):
#     print(fields)
#     for key, value in fields.items():
#         print(key, value)
# details(name="Prince",age=20,job="Engineer")
# numbers=[1,8,5,0,8,9,0,8,0]
# nums = [1,2,3,4,5,6,7,8,9]
# square=list(map(lambda x,y: x+y,numbers, nums))
# print(square)

# numbers=[1,8,5,0,8,9,0,8,0]
#
# square=list(filter(lambda x: x>0,numbers))
# squar=list(map(lambda x: x>0,numbers))
# print(square)
# print(squar)
# addi=(reduce(lambda x,y:x+y,numbers))
# print(addi)
#
# for i,val in enumerate(numbers):
#     print(i,val)
# ce=[30,40]
# def ctof(c):
#     print ( c*(9/5)+32)
# ctof(30)
#
# cto=list(map(lambda x: (x*(9/5)+32),ce))
# print(cto)

