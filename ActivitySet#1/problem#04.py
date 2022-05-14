hrs = input("Enter Hours:")
h = float(hrs)
r=input("Enter the rate:")
z=float(r)
if(h<40):
  m=h*z
  print(m)
elif(h>40):
  t=h-40
  k=t*1.5*z+40*z
  print(k)
  
  
