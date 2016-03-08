__author__ = 'acpb859'
list = [0,1,2,3,4]
list2 = []
for x in list:
    list2.append(x * 0.5)

print(list2)

list3 = []
for x in list2:
    if x <1.5:
        list3.append(x)
print(list3)