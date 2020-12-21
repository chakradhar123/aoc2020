lines=[]
line=input()
HashMap={}
totalLines=[]
while (line!='end'):
    line=line.split(' ')
    if '(contains' in line:
        
        index=line.index('(contains')
        lines.extend(line[:index])
        for i in range(index+1,len(line)):
            if line[i][:-1] in HashMap:
                HashMap[line[i][:-1]]=HashMap[line[i][:-1]].intersection(lines)
            else:
                HashMap[line[i][:-1]]=set(lines)
        totalLines.extend(lines)
        lines=[]
        line=input()
        continue

    lines.extend(line)
    line=input()
finalMap=set()
# for value in HashMap.values():
#     finalMap=finalMap.union(value)
count=0
allSet=[]

for key in HashMap.keys():
    allSet.append(key)
visited=set()
while count!=len(allSet):
    for i in range(0,len(allSet)):
        if(len(HashMap[allSet[i]])==1) and (allSet[i] not in visited):
            visited.add(allSet[i])
            for j in range(0,len(allSet)):
                if j!=i:
                    HashMap[allSet[j]]=HashMap[allSet[j]].symmetric_difference(HashMap[allSet[j]].intersection(HashMap[allSet[i]]))
    count+=1
allSet.sort()
finalStr=""
for i in range(0,len(allSet)):
    for j in HashMap[allSet[i]]:
        if i !=len(allSet)-1:
            finalStr=finalStr+j+','
        else:
            finalStr=finalStr+j
        
    
print(finalStr)