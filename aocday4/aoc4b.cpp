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
 if(line=="")
    v.push_back(line);
    else{
        string curr="";
        for(int i=0;i<(int)line.length();i++){
            if(line[i]==' '){
                v.push_back(curr);
                curr="";
            }else{
                curr+=line[i];
            }
        }
        v.push_back(curr);
    }
  }

int checkPass[7]={0};
      for(int i=0;i<(int)v.size();i++){
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
              continue;
          }
          string curr="";
          curr+=v[i][0];
          curr+=v[i][1];
          curr+=v[i][2];
        
        string  rest=v[i].substr(4);
        
          if(curr=="byr"){
                     
                    int year=stoi(rest);
                    if(year>=1920&&year<=2002){
                        checkPass[0]=1;
                    }
                  }
                  if(curr=="iyr"){
                      int year=stoi(rest);
                    if(year>=2010&&year<=2020){
                        checkPass[1]=1;
                    }
                  }
                  if(curr=="eyr"){
                      int year=stoi(rest);
                    if(year>=2020&&year<=2030){
                        checkPass[2]=1;
                    }
                  }
                  if(curr=="hgt"){
                    
                      string last2=rest.substr(((int)rest.length())-2);
                      if(last2=="cm"){
                          int num=stoi(rest.substr(0,((int)rest.length())-2));
                          if(num>=150&&num<=193)
                            checkPass[3]=1;
                      }
                      if(last2=="in"){
                          int num=stoi(rest.substr(0,((int)rest.length())-2));
                          if(num>=59&&num<=76)
                            checkPass[3]=1;
                      }
                  }
                  if(curr=="hcl"){
                      
                      if(rest[0]=='#'&&((int)rest.length())==7){
                          int flag=1;
                          for(int j=1;j<7;j++){
                              if(rest[j]>='0'&&rest[j]<='9'){
                                continue;
                              }
                               if(rest[j]>='a'&&rest[j]<='f'){
                                continue;
                              }
                              flag=0;
                              break;
                          }
                          if(flag){
                              checkPass[4]=1;
                          }
                      }

                  }
                  if(curr=="ecl"){
                      if(rest=="amb"||rest=="blu"||rest=="brn"||rest=="gry"||rest=="grn"||rest=="hzl"||rest=="oth")
                      checkPass[5]=1;
                  }
                  if(curr=="pid"){
                      
                     
                      if(((int)rest.length())==9){
                          int flag=1;
                          for(int j=0;j<(int)rest.length();j++){
                              if(rest[j]>='0'&&rest[j]<='9'){
                                continue;
                              }
                              flag=0;
                              break;
                          }
                          if(flag)
                          checkPass[6]=1;
                      }
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