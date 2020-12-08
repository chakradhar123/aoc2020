lines=[]
line=input()
while (line!='end'):
    lines.append(line.split(' '))
    line=input()


visited=[0 for line in lines]

curr=0
acc=0

while True:

    if visited[curr]:
        print(acc)
        break
    visited[curr]=1;
    if lines[curr][0]=='acc':
        acc=(acc+int(lines[curr][1][1:])) if (lines[curr][1][0]=='+') else (acc-int(lines[curr][1][1:]))
        curr+=1
        continue
    if lines[curr][0]=='nop':
        curr+=1
        continue
    curr=(curr+int(lines[curr][1][1:])) if (lines[curr][1][0]=='+') else (curr-int(lines[curr][1][1:]))