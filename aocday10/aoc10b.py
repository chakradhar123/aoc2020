lines=[]
line=input()
while (line!='end'):
    lines.append(int(line))
    line=input()
lines=sorted(lines)
lines.insert(0,0)
lines.append(lines[-1]+3)
def tribanocci(num):
    if num==1:
        return 1
    if num==2:
        return 1
    if(num==3):
        return 2
    return tribanocci(num-1)+tribanocci(num-2)+tribanocci(num-3)

ans=1
currsize=1
for i in range(1,len(lines)):
    if lines[i]-lines[i-1]<=2:
        currsize+=1
    else:
   
        ans*=tribanocci(currsize)
        currsize=1
ans*=tribanocci(currsize)
print(ans)
