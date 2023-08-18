f1=open("one.txt",'w')
f1.write("welcome to the file handeling \n")
f1.write("vanakkam \n")
f1.close()

f2=open("one.txt",'r')
print(f2.read(3))
print(f2.readline())
f2.close()




