import re
hand = open('ref2.txt')

m=hand.read()
x = re.findall('([0-9]+)', m)
print(x)
z=0
for i in x:
       z=z+int(i)
print(z)