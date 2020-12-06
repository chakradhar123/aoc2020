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
int a[26]={0},ans=0;
for(int i=0;i<(int)v.size();i++){
    if(v[i]==""){
for(int j=0;j<26;j++){
    if(a[j]){
        ans++;
    }
        a[j]=0;
    }
    }
    
    for(int j=0;j<(int)v[i].length();j++){
        a[v[i][j]-'a']++;
    }
}
for(int j=0;j<26;j++){
    if(a[j]){
        ans++;
    }
 
    }
cout<<ans<<endl;

}
