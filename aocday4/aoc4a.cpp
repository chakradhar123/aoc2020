#include<bits/stdc++.h>
using namespace std;




int main(){
  vector<string> v;
  string line;
  int validPassports=0;
  while(getline(cin,line)){
    
  if(line =="end"){
    break;
  }
 
    v.push_back(line);
  }
int checkPass[7]={0};
      for(int i=0;i<v.size();i++){
          if(v[i]==""){
              int flag=1;
              for(int j=0;j<7;j++){
                  if(checkPass[j]==0){
                      flag=0;
                      
                  }
                  checkPass[j]=0;
              }
              if(flag){
                  validPassports++;
              }
          }else{
              int j=0;
              do{
             string curr="";
             curr+=v[i][j];
             curr+=v[i][j+1];
             curr+=v[i][j+2];
             
                  if(curr=="byr"){
                      checkPass[0]=1;
                  }
                  if(curr=="iyr"){
                      checkPass[1]=1;
                  }
                  if(curr=="eyr"){
                      checkPass[2]=1;
                  }
                  if(curr=="hgt"){
                      checkPass[3]=1;
                  }
                  if(curr=="hcl"){
                      checkPass[4]=1;
                  }
                  if(curr=="ecl"){
                      checkPass[5]=1;
                  }
                  if(curr=="pid"){
                      checkPass[6]=1;
                  }
while(j<(int)v[i].length()&&v[i][j]!=' '){
    j++;
}
j++;
              }while(j<(int)v[i].length());
          }

      }
       int flag=1;
      for(int j=0;j<7;j++){
                  if(checkPass[j]==0){
                      flag=0;
                      
                  }
                  checkPass[j]=0;
              }
              if(flag){
                  validPassports++;
              }

 
 cout<<validPassports<<endl;

}