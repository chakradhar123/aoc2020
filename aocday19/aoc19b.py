import re
lines=[]
lineDict={}
line=input()
while (line!='end'):
    if ':' in line:
        line=line.split(': ')
       
        lineDict[line[0]]=line[1]

    elif line!='':    
        lines.append(line)
    line=input()


lineDict['8']='42 | 42 8'
lineDict['11']='42 31 | 42 11 31'
def find(key,n):
    if n==20:
        return ''
    if lineDict[key][0]=='"':
        return lineDict[key][1]
    return '('+'|'.join([''.join([find(item,n+1) for item in s.split(' ')]) for s in lineDict[key].split(' | ')])+')'

r = re.compile(find('0',0))

print(sum([bool(r.fullmatch(line)) for line in lines]))