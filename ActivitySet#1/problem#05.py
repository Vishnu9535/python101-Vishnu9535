def computepay(h,r):
  if(h<40):
    z=h*r
  elif(h>40):
    m=h-40
    z=m*1.5*r+40*r
    return z

hrs=input("Enter number of hours")
h=float(hrs)
rate=input("Enter the rate")
r=float(rate)
z=computepay(h,r)
print("Pay",z)
