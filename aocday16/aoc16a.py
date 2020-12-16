lines=[]
line=input()
yourIndex=0
nearIndex=0
index=0
while (line!='end'):
    if line=="":
        line=input()
        continue
    if line=="your ticket:":
        yourIndex =index
        nearIndex=index+1
        line=input()
        continue
    if line=="nearby tickets:":
        line=input()
        continue
    if yourIndex:
        lines.append(line.split(','))
        
    else:
        lines.append(line.split(': ')[1].split(' or '))
    
    index+=1
    line=input()
for i in range(0,len(lines)):
    if i<yourIndex:
        lines[i][0]=lines[i][0].split('-')
        lines[i][1]=lines[i][1].split('-')
        lines[i][0][0]=int(lines[i][0][0])
        lines[i][0][1]=int(lines[i][0][1])
        lines[i][1][0]=int(lines[i][1][0])
        lines[i][1][1]=int(lines[i][1][1])
    else:
        for j in range(0,len(lines[i])):
            lines[i][j]=int(lines[i][j])

ans=0
for i in range(nearIndex,len(lines)):
    for j in range(0,len(lines[i])):
        flag=1
        for k in range(0,yourIndex):
            if lines[i][j]>=lines[k][0][0] and lines[i][j]<=lines[k][0][1]:
                flag=0
                break
            if lines[i][j]>=lines[k][1][0] and lines[i][j]<=lines[k][1][1]:
                flag=0
                break
        if flag:
            ans+=lines[i][j]
print(ans)