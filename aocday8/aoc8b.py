lines=[]
line=input()
while (line!='end'):
    lines.append(line.split(' '))
    line=input()


def checkLines(lines):

    visited=[0 for line in lines]

    curr=0
    acc=0

    while True:
        if curr>=len(lines):
       
            return True,acc
        if visited[curr]:
            return False,0
       

        
        visited[curr]=1
        if lines[curr][0]=='acc':
            acc=(acc+int(lines[curr][1][1:])) if (lines[curr][1][0]=='+') else (acc-int(lines[curr][1][1:]))
            curr+=1
            continue
        if lines[curr][0]=='nop':
            curr+=1
            continue
        curr=(curr+int(lines[curr][1][1:])) if (lines[curr][1][0]=='+') else (curr-int(lines[curr][1][1:]))
    
for line in lines:
    if line[0]=='nop':
        line[0]='jmp'
        flag,acc=checkLines(lines)
        if flag:
            print(acc)
            break
        else:
            line[0]='nop'
        
    if line[0]=='jmp':
        line[0]='nop'
        flag,acc=checkLines(lines)
        if flag:
            print(acc)
            break
        else:
            line[0]='jmp'
      