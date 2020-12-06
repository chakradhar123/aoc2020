#include<bits/stdc++.h>
using namespace std;

int main(){
  vector<string> v;
  string line;
  int validPasswords=0;
  while(getline(cin,line)){
    
  if(line =="end"){
    break;
  }
    v.push_back(line);
  }
int a[26]={0},b[26]={0},ans=0,flag=1,flag2=1;
for(int i=0;i<(int)v.size();i++){
    if(v[i]==""){
        if(flag){
for(int j=0;j<26;j++){
if(b[j]){
    ans++;
}
b[j]=0;
}
        }else{
for(int j=0;j<26;j++){
    if(a[j]){
    ans++;
}
a[j]=0;
}
        }

flag2=1;
flag=1;
continue;
    }
    for(int j=0;j<(int)v[i].length();j++){
        if(flag2){
       
a[v[i][j]-'a']=1;
        
        }else{
        if(flag){
            if(b[v[i][j]-'a']){
                a[v[i][j]-'a']=1;
            }
        }else{
if(a[v[i][j]-'a']){
            b[v[i][j]-'a']=1;
            }
        }
        }
        
    }
 
        if(flag){
for(int j=0;j<26;j++){
b[j]=0;
}
        }else{
for(int j=0;j<26;j++){
    a[j]=0;
}
        }
    flag2=0;
    flag=flag^1;

}

 
      if(flag){
for(int j=0;j<26;j++){
if(b[j]){
    ans++;
}
}
        }else{
for(int j=0;j<26;j++){
    if(a[j]){
    ans++;
}
}
        }
cout<<ans<<endl;

}
