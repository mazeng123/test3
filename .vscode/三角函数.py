a,b,c=map(int,input().split())
max1=max(a,b,c)
min1=min(a,b,c)
for i in range(1,min1+1):
    if max1%i==0 and min1%i==0:
        max1=max1//i
        min1=min1//i
#print(min1,"/",max1)
print(f'{min1}/{max1}')