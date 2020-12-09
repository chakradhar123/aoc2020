lines=[]
line=input()
while (line!='end'):
    lines.append(int(line))
    line=input()

hashDict={}
preLen=25
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
        print(lines[i])
        break
    if lines[i] in hashDict:
        hashDict[lines[i]]+=1
    else:
        hashDict[lines[i]]=1

    hashDict[lines[i-25]]-=1