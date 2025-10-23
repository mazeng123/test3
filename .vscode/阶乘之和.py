n=input()
n=int(n)
sum1=0
s1=1
for i in range(1,n+1):
    for j in range(1,i+1):
        s1=s1*j
    sum1=sum1+s1
    s1=1
print(sum1)