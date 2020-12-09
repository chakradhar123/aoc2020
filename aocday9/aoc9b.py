lines=[]
line=input()
while (line!='end'):
    lines.append(int(line))
    line=input()

hashDict={}
preLen=25
invalid=-1
for i in range(0,preLen):
    if lines[i] in hashDict:
        hashDict[lines[i]]+=1
    else:
        hashDict[lines[i]]=1
    

for i in range(preLen,len(lines)):
    flag=0

    for j in range(i-preLen,i):
        if lines[i]-lines[j] in hashDict:
            if lines[i]-lines[j]==lines[j]:
                if hashDict[lines[i]-lines[j]]>1:
                    flag=1
            elif  hashDict[lines[i]-lines[j]]>0:
                flag=1
                break
    if flag==0:
        invalid=lines[i]
        break
    if lines[i] in hashDict:
        hashDict[lines[i]]+=1
    else:
        hashDict[lines[i]]=1

    hashDict[lines[i-25]]-=1


currsum=lines[0]+lines[1]
l=0
r=1
while r<len(lines):
    if currsum==invalid:
        break
    if currsum<invalid or r-l<=1:
        r+=1
        if r<len(lines):
            currsum+=lines[r]
    else:
        currsum-=lines[l]
        l+=1
ma=-1
mi=-1
for i in range(l,r+1):
    if(lines[i]>ma):
        ma=lines[i]
    if mi==-1 or lines[i]<mi:
        mi=lines[i]
print(ma+mi)