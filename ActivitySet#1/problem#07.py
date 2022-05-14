def find():
     str = 'X-DSPAM-Confidence:0.8475'
     vis=str[19:25]
     man=float(vis)
     return man
man=find()
print(man)


