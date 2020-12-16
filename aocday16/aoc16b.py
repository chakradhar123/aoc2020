import copy
lines=[]
departureIndex=[]
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
        if(line.split(': ')[0].split(' ')[0]=='departure'):
            departureIndex.append(index)

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
temp=[1 for i in range(0,yourIndex)]
checkArr=[copy.deepcopy(temp)for i in range(0,len(lines[yourIndex]))]
invalid=set()
for i in range(nearIndex,len(lines)):
    for j in range(0,len(lines[i])):
        flag=1
        for k in range(0,yourIndex):
            if lines[i][j]>=lines[k][0][0] and lines[i][j]<=lines[k][0][1]:
                flag=0
                
            if lines[i][j]>=lines[k][1][0] and lines[i][j]<=lines[k][1][1]:
                flag=0
                
        if flag:
            invalid.add(lines[i][j])

for i in range(0,len(lines[yourIndex])):
    for j in range(nearIndex,len(lines)):
        if lines[j][i] in invalid:
            continue
        
        for k in range(0,yourIndex):
            flag=1
            if lines[j][i]>=lines[k][0][0] and lines[j][i]<=lines[k][0][1]:
                flag=0
                
            if lines[j][i]>=lines[k][1][0] and lines[j][i]<=lines[k][1][1]:
                flag=0
            if flag:

                checkArr[i][k]=0


finalArr=[]
for i in checkArr:
    finalArr.append([j for j in range(0,len(i)) if i[j]==1])


temp=[-1 for i in range(0,yourIndex)]
curr=1
filled=0
while filled!=len(temp):
    for p in range(0,len(finalArr)):
        if(len(finalArr[p])==curr):
            for i in range(0,curr):
                if temp[finalArr[p][i]]==-1:
                    temp[finalArr[p][i]]=p
                    filled+=1
    curr+=1

ans=1
for i in range(0,len(departureIndex)):
    ans*=lines[yourIndex][temp[departureIndex[i]]]

print(ans)