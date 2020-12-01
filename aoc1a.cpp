#include<bits/stdc++.h>
using namespace std;

int main(){
  vector<int> v;
  string line;
  while(getline(cin,line)){
    
  if(line =="end"){
    break;
  }
    v.push_back(stoi(line));
  }
  unordered_set<int>uset;
  int ans=-1;
  for(int i=0;i<(int)v.size();i++){
if(uset.find(2020-v[i])!=uset.end()){
ans=v[i]*(2020-v[i]);
break;
}
uset.insert(v[i]);
  }
  cout<<ans<<endl;


}
