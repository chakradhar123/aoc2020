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
  int height=(int)v.size();
  int width=(int)v[0].length();
  int currRow=0,i=0,j=0,trees=0;
  do{
      i+=1;
      j+=3;
      j%=width;
if(v[i][j]=='#'){
    trees++;
}
// cout<<i<<" "<<j<<" "<<v[i][j]<<endl;

  }while(i!=height-1);
cout<<trees<<endl;

}