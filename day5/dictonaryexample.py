d1={101:'abc',102:"def"}
print(type(d1))
print(d1[101])

d1.pop(101)
print(d1)

d1[103]='xyz'
d1[101]='abc'
d1[102]='hello'
print(d1)

