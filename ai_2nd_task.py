n = int(input("Enter a number :  "))
x = 0
y = 1
count = 0
if n <= 0:
   print("Please enter a positive number ")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(x)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(x)
       nth = x + y
       x = y
       y = nth
       count = count + 1
