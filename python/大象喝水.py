pi=3.14
h,r= input().split()
r=int(r)
h=int(h)
sum1=pi*r*r*h
count=20*1000/sum1
count=int(count)+1
print(count)
