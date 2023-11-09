from math import sqrt
import math

lower = 500
upper = 5000

print(" total Prime numbers between", lower, "and", upper, "are: ")
total=0
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           total+=1
print(f"There are total {total} prime numbers between 500 and 5000 ")


prime = [0 for i in range(total)]
j=0
safe_prime = [0 for i in range(total)]


for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime[j] = num
           j+=1

print(prime)
k=0
for num in prime:
    safe_prime[k]=(prime[k]-1)//2
    k+=1


#loop for safe numbers finding among prime numbers
print(f"ALL Safe prime numbers between 500 and 5000")
for num in safe_prime:
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           if num>500 and num<5000:
             #print(num)