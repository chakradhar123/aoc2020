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
unordered_set<int>uset;
int id1,id2;
for(int i=0;i<(int)v.size();i++){
int lRow=0,rRow=127,lCol=0,rCol=7;
int currRow=lRow+(rRow-lRow)/2;
int currCol=lCol+(rCol-lCol)/2;

for(int j=0;j<7;j++){
    if(v[i][j]=='F'){
        rRow=currRow;
    }else{
        lRow=currRow+1;
    }
   currRow= lRow+(rRow-lRow)/2;
}
for(int j=7;j<10;j++){
    if(v[i][j]=='L'){
        rCol=currCol;
    }else{
        lCol=currCol+1;
    }
   currCol= lCol+(rCol-lCol)/2;
   
}
int id=currRow*8+currCol;
  
   uset.insert(id);

}

for(auto x:uset){
int num=(x);
if(uset.find(num-1)==uset.end()&&uset.find(num-2)!=uset.end()){
    cout<<num-1<<endl;
}
}

}