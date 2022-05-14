fname=input("Enter the file name")
xam=open(fname)
count=0
cam=list()
for line in xam:
    if not line.startswith("From:"):
        continue
    count=count+1
    cam=line.split()
    print(cam[1])
print("There were", count, "lines in the file with From as the first word")

    
    