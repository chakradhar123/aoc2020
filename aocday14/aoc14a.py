lines=[]
line=input()
while (line!='end'):
    line=line.split(" = ")
    if line[0]!="mask":
        line[1]=int(line[1])
        line[0]=int(line[0][4:-1])
    lines.append(line)
    line=input()
lineDict={}

mask=""
for line in lines:
    if line[0]=="mask":
        mask=line[1]
        mask=mask[::-1]
    else:
        temp=line[1]
        curr=1
        val=0
        
        for i in range(0,36):
            if mask[i]=='X':
                if temp%2==1:
                    val+=curr
            else:
                if mask[i]=='1':
                    val+=curr
            
            curr*=2
            temp//=2
        
        
        lineDict[line[0]]=val
ans=0
for key,value in lineDict.items():
    ans+=value

print(ans)