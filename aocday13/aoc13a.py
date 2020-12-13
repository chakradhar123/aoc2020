line1=int(input())
line2=input().split(',')
ans=line1
ans1=0
for item in line2:
    if item!="x":
        n=int(item)
        if line1%n!=0:
            temp=line1//n
            temp=temp+1
            temp=temp*n
            if temp-line1<ans:
                ans=temp-line1
                ans1=n
print(ans*ans1)

