from functools import reduce

names = ["Alice", "Bob", "Charlie","asd"]
# scores = [90, 85, 95,67]
#
# combined = list(zip(names, scores))
# print(combined)


# for i,val in enumerate(names):
#     print(i,val)
#     print(val)
#
# l=list(enumerate(scores))
# print(l)


# def conti(name):
#     c=0
#     for char in name:
#         c+=1
#     return c


li=list(filter(lambda x:len(x)>4, names))
lis=list(map(lambda x:x.upper(), li))
print(lis)

l1=reduce(lambda x,y:x+y, names)
print(l1)