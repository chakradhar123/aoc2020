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



def find(key):
    if lineDict[key][0]=='"':
        return lineDict[key][1]
    return '('+'|'.join([''.join([find(item) for item in s.split(' ')]) for s in lineDict[key].split(' | ')])+')'

r = re.compile(find('0'))

print(sum([bool(r.fullmatch(line)) for line in lines]))