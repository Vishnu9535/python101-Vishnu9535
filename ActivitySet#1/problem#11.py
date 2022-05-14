fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts=dict()
for line in fhand :
    if line.startswith('From:'):
        if line[6:] not in counts:
            counts[line[6:]]=1
        else:
            counts[line[6:]]+=1
words=counts.values()
zam=max(words)
for key in counts:
    if counts[key]==zam:
        print(key, counts[key])