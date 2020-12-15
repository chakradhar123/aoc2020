lines=input().split(',')
lineDict={}
for i in range(0,len(lines)):
    lines[i]=int(lines[i])
    lineDict[lines[i]]=i+1
lines.append(0)
for i in range(len(lines),30000000):

    if lines[i-1] in lineDict:
        lines.append(i-lineDict[lines[i-1]])
    else:
        lines.append(0)

    lineDict[lines[i-1]]=i

print(lines[30000000-1])

