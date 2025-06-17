# li=["ram",1,"2w"]
# lq=li
# li[1]=2
#
# print(li)
# print(lq)
# lq.append(3)
# print(li)
# print(lq)
#
# lq.insert(2,"Rwa")
# print(li)
# print(lq)
# lq.pop()
# print(li)
# print(lq)
# lq.remove("ram")
#
# print(li)
# print(lq)
# lq.pop(1)
# print(li)
# print(lq)


# tupp=(1,3,"sd",4)
# print(tupp)
# print(tupp[0])
# tupp.pop()
# print(tupp)


# set={1,4,2,2,1,5,2,3}
# print(set)
# for char in set:
#     print(char)

keyValDict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(keyValDict)
print(keyValDict["a"])
print(keyValDict.items())

for k in keyValDict.items():
    print(k[0]*k[1])
keyValDict["3"]=4
print(keyValDict)

