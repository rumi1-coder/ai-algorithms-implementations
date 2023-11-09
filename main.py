import math
savefile=open('my_file.txt','w')
def f(x):
   m=1.2
   s=2
   y=1/(math.sqrt(2*math.pi*s))*math.exp(-1/2*(x-m)/s**2)
   print(f'y={y}')
   savefile.write(str(y))

print('values of the function for m=1.2 ,s=2,-20<x<20')
for x in range(-19,20):
    f(x)

print('Data also saved to "my_file.txt"')
savefile.close()



