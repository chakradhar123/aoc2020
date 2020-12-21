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
for value in HashMap.values():
    finalMap=finalMap.union(value)
count=0
for line in totalLines:
    if line not in finalMap:
        count+=1

print(count)