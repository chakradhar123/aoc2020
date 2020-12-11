lines=[]
line=input()
while (line!='end'):
    lines.append(int(line))
    line=input()
lines=sorted(lines)
ones=0
three=1
if lines[0]==1:
    ones=1
if lines[0]==3:
    three+=1
for i in range (1,len(lines)):
    if lines[i]-lines[i-1]==1:
        ones+=1
    if lines[i]-lines[i-1]==3:
        three+=1
print(ones*three)