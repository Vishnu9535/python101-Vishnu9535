largest = None
smallest = 10000000
while True:
  
  num = input("Enter a number: ")
  try:
    if num == "done":
      break
    k=int(num)
  except:
    print('Invalid input')
    
  if largest is None:
      largest=k
  elif largest<k:
      largest=k
  if k<smallest:
      smallest =k      
print("Maximum is", largest)
print("Minimum is",smallest)
