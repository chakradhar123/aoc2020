lines=[]
line=input()
while (line!='end'):
    lines.append(line.split(' '))
    line=input()

linesDict={}
for line in lines:
    line[0]=line[0]+line[1]
    line.pop(1)
    line.pop(1)
    line.pop(1)
    
    if line[1]=='no':
        continue
    curr=2
    while curr<len(line):
        temp=line[curr]+line[curr+1]
        if temp in linesDict:
            linesDict[temp].add(line[0])
        else:
            linesDict[temp]=set()
            linesDict[temp].add(line[0])
        curr+=4

count=0
visited=set()
queue=[]
queue.append('shinygold')
while len(queue)!=0:
    if queue[0] in linesDict:
        for value in linesDict[queue[0]]:
            if value in visited:
                continue
            count+=1
            if value=='shinygold':
                visited.add(value)
                continue
            queue.append(value)
            visited.add(value)
            
    queue.pop(0)



print(count)

    