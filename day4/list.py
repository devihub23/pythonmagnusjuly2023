a1=[10,11,12,"abc",'def']

print(a1)
print(a1[0:5])
print(a1[1:3])
print(a1[:2])
print(a1[2:])
a1.append(120)
print(a1)
a1.insert(3,'hi')
print(a1)
a1[2]=2
print(a1)
a1.remove('hi')
print(a1)

a1.pop()
print(a1)
a1.pop(2)
print(a1)

