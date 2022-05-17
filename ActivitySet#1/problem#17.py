fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
x=dict()
for line in fhand :
    if line.startswith('From') and not line.startswith("From:"):
        man=line.split()
        zam=man[5].split(':')
        if zam[0] not in x:
            x[zam[0]]=1
        else:
            x[zam[0]]+=1
z=list(x.items())
z.sort()

for keys,values in z:
    print(keys,values)
        
        



        
        
        