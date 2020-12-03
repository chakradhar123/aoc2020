#include<bits/stdc++.h>
using namespace std;

int goDown(vector<string> &v,int right,int down){
 int height=(int)v.size();
  int width=(int)v[0].length();
  int currRow=0,i=0,j=0,trees=0;
  do{
      i+=down;
      j+=right;
      j%=width;
      if(i==height){
          break;
      }
if(v[i][j]=='#'){
    trees++;
}
// cout<<i<<" "<<j<<" "<<v[i][j]<<endl;

  }while(i!=height-1);
return trees;
}
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
 cout<<goDown(v,1,1)*goDown(v,3,1)*goDown(v,5,1)*goDown(v,7,1)*goDown(v,1,2)<<endl;

}