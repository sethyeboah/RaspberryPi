# Fibonacci series
a, b = 0, 1
print(a, end=',')
while b < 1000:
    print(b, end=',')
    a, b = b,(a+b) # Expressions on the right-hand side are all evaluated first before any of the assignments take place

