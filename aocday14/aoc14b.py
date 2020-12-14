import itertools
import copy 
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
bitPos=[]
for line in lines:
    if line[0]=="mask":
        mask=line[1]
   
        bitPos=[]
        ones=[]
        for i in range(0,36):
            if mask[i]=='X':
                bitPos.append(i)
            if mask[i]=='1':
                ones.append(i)
        bitPos.reverse()
    else:
        binary=format(line[0], "036b")
        binary=list(binary)
        temp=line[0]
        curr=0
        for i in ones:
            binary[i]='1'
        
        for item in itertools.product(('0','1'),repeat=len(bitPos)):
            
            binTemp=copy.deepcopy(binary)
            for pos,bit in zip(bitPos,item):
                binTemp[pos]=bit
            lineDict[int(''.join(binTemp),2)]=line[1]

        
        

ans=0
for key,value in lineDict.items():
    ans+=value

print(ans)