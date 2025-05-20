i = 0
for i in range(101):
  if i % 3 == 0 and i % 5 == 0:
    i = "FizzBuzz"
    print(i)  
  elif i % 3 == 0:
    i = "fizz"
    print(i)
  elif i % 5 == 0:
    i = "Buzz"
    print(i)
  else:  
    print(i)
