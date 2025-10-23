import math
l=int(input())
sum1=0
count=0
i=2
number=[]
while sum1<=l:
    flag=1
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            flag=0
    if flag==1:
        sum1+=i
        number.append(i)
        count+=1
    i+=1
for num in range(len(number)-1):
    print(number[num])
print(count-1)
