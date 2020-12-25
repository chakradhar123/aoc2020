c=int(input())
d=int(input())
i=1
j=1
count1=0
count2=0
while(i!=c):
    
    i*=7
    i%=20201227
    count1+=1

while(j!=d):
    j*=7
    j%=20201227
    count2+=1

ans=1
for i in range(0,count2):
    ans*=c
    ans%=20201227
print(ans)
