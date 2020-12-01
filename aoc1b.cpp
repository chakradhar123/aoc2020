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
      unordered_set<int>uset;
    for(int j=i+1;j<(int)v.size();j++){
        if(uset.find(2020-(v[i]+v[j]))!=uset.end()){
        ans=v[i]*v[j]*(2020-v[i]-v[j]);
        break;
        }
        uset.insert(v[j]);
    }
    if(ans!=-1){
        break;
    }
  }

cout<<ans<<endl;
}