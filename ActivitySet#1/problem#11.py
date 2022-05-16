fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts=dict()
man=list()
for line in fhand :
    if line.startswith('From:'):
        man=line.split()
        if man[1] not in counts:
            counts[man[1]]=1
        else:
            counts[man[1]]+=1
words=counts.values()
zam=max(words)
for key in counts:
    if counts[key]==zam:
        print(key,zam)
        
        
