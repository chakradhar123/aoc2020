lines=[]
line=input()

while (line!='end'):
    lines.append(line)
    line=input()
stackV=[]
stackO=[]
ans=0
for line in lines:
    for letter in line:
        if letter==' ':
            continue
        elif letter=='+' or letter=='*' or letter=='(':
            if len(stackO)==0 or letter=='(':
                stackO.append(letter)
            elif letter=='*':
                while len(stackO)!=0 and stackO[-1]=='+':
                    temp1=stackV[-1]
                    stackV.pop()
                    temp2=stackV[-1]
                    stackV.pop()
                    stackO.pop()
                    stackV.append(temp1+temp2)
                stackO.append(letter)
            else:
                stackO.append(letter)

        elif letter==')':
            while stackO[-1]!='(':
                op=stackO[-1]
                temp1=stackV[-1]
                stackV.pop()
                temp2=stackV[-1]
                stackV.pop()
                stackO.pop()
                if op=='+':
                    stackV.append(temp1+temp2)
                else:
                    stackV.append(temp1*temp2)
            stackO.pop()

        else:
            stackV.append(int(letter))
    
    while len(stackO)!=0:
        op=stackO[-1]
        temp1=stackV[-1]
        stackV.pop()
        temp2=stackV[-1]
        stackV.pop()
        stackO.pop()
        if op=='+':
            stackV.append(temp1+temp2)
        else:
            stackV.append(temp1*temp2)
    ans+=stackV[-1]
    stackV=[]
    stackO=[]
print(ans)