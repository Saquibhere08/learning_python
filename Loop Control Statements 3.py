#while & Continue
#for prime numbers
num=int(input("ENter a number: "))
d=2
while num>1:
    if num%d==0:
        print(d)
        num=num/d
        continue
    d=d+1
