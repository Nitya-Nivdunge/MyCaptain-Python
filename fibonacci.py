num = int(input("Enter no. of terms of the series you want to print : "))
t1,t2 = 0, 1
count = 1
print("Fibonacci sequence:")
while count < num:
  print(t1)
  temp = t1 + t2
  t1 = t2
  t2 = temp
  count += 1
