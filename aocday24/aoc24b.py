from collections import defaultdict
lines=[]
lin=input()
while (lin!='end'):
    lines.append(lin)
    lin=input()


tileDict=defaultdict(int)

for line in lines:
    x=0
    y=0
    z=0
    j=0
    while j<len(line):
        if line[j]=='e':
            x+=1
            y-=1
            j+=1
        elif line[j]=='w':
            x-=1
            y+=1
            j+=1
        elif line[j]+line[j+1]=='nw':
            y+=1
            z-=1
            j+=2
        elif line[j]+line[j+1]=='ne':
            x+=1
            z-=1
            j+=2
        elif line[j]+line[j+1]=='sw':
            x-=1
            z+=1
      
            j+=2
        elif line[j]+line[j+1]=='se':
            y-=1
            z+=1
            j+=2
        
    tileDict[(x,y,z)]=1 if tileDict[(x,y,z)]==0 else 0
        

blackDict=set()
def getNeigh(tple):
    return [tuple([tple[i]+d[i] for i in range(3)]) for d in[(1,-1,0), (1,0,-1), (0,1,-1), (-1,1,0), (-1,0,1), (0,-1,1)]]

for key,val in tileDict.items():
    if(val==1):
        blackDict.add(key)
for i in range(0,100):
    newBlack=set()
    for item in blackDict:
        neighbours=getNeigh(item)
        count=0
        for n in neighbours:
            if n in blackDict:
                count+=1
        if count!=0 and count<=2:
            newBlack.add(item)
        for n in neighbours:
            if n not in blackDict:
                neighbours2=getNeigh(n)
                count=0
                for n1 in neighbours2:
                    if n1 in blackDict:
                        count+=1
                if count==2:
                    newBlack.add(n)
    blackDict=set([p for p in newBlack])
        
print(len(blackDict))