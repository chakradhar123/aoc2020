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
        

print(sum(tileDict.values()))
