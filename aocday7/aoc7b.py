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
    temp=line[0]
    linesDict[temp]={}
    while curr<len(line):
        linesDict[temp][line[curr]+line[curr+1]]=int(line[curr-1])
        
        curr+=4

def getValue(color):
    if color not in linesDict:
        return 0
    count=0
    for item,value in linesDict[color].items():
        if item in linesDict:
            count+=value+value*getValue(item)
        else:
            count+=value
    return count
print(getValue('shinygold'))


    