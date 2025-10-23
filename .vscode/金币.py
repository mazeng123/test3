k=int(input())
sum1=0
a=k
for i in range(1,k+1):
    if a==0: break
    else:
        for j in range(1,i+1):
            sum1=sum1+i
            a-=1
            if a == 0: break
print(sum1)