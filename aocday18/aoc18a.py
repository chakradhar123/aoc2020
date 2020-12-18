lines=[]
line=input()

while (line!='end'):
    lines.append(line)
    line=input()
stack=[]
ans=0
for line in lines:
    for letter in line:
        if letter==' ':
            continue
        elif letter=='+' or letter=='*' or letter=='(':
            stack.append(letter)
        elif letter==')':
            temp=stack[-1]
            stack.pop()
            stack.pop()
            if len(stack)==0 or (stack[-1]!='+' and stack[-1]!='*'):
                stack.append(temp)
            else:
                temp1=stack[-1]
                stack.pop()
                temp2=stack[-1]
                stack.pop()
                if temp1=='+':
                    stack.append(temp2+temp)
                else:
                    stack.append(temp2*temp)

        else:
            if len(stack)==0 or (stack[-1]!='+' and stack[-1]!='*'):
                stack.append(int(letter))
            else:
                temp=stack[-1]
                stack.pop()
                temp2=stack[-1]
                stack.pop()
                if temp=='+':
                    stack.append(temp2+int(letter))
                else:
                    stack.append(temp2*int(letter))
    ans+=stack[-1]
   
    stack=[]
print(ans)