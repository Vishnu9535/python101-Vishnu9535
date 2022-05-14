v=input('enter the file name')
x=open(v)
count=0
m=0
for line in x:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    z=float(line[20:26])
    m=z+m
print('Average spam confidence:',m/count)    