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
  for(int i=0;i<(int)v.size();i++){

      string numStringLow="",numStringHigh="";
      bool dashFound=false;
      int j=0;
      for(;j<(int)v[i].length();j++){
          if(v[i][j]==' '){
              j++;
            break;
          }
          if(v[i][j]=='-'){
              dashFound=true;
              continue;
          }
          if(dashFound){
              numStringHigh+=v[i][j];
          }else{
              numStringLow+=v[i][j];
          }
          
      }
      int low=stoi(numStringLow),high=stoi(numStringHigh);
      char key=v[i][j];
      j+=3;
      
      
      if(v[i][j+low-1]==key&&v[i][j+high-1]==key){
          continue;
      }
      if(v[i][j+low-1]==key){
          validPasswords++;
      }
      if(v[i][j+high-1]==key){
          validPasswords++;
      }
  }
  cout<<validPasswords<<endl;

}
