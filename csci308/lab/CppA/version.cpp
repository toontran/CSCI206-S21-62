#include<iostream>
using namespace std;
/* This program will tell which standard of C++ you are currently using. */
int main(){
  // The magic numbers are the year and month that the standard was approved
  if( __cplusplus == 201703L ) std::cout << "C++17\n" ;
  else if( __cplusplus == 201402L ) std::cout << "C++14\n" ;
  else if( __cplusplus == 201103L ) std::cout << "C++11\n" ;
  // 2003 has too few revisions to be considered a standard
  else if( __cplusplus == 199711L ) std::cout << "C++98\n" ;
  else std::cout << "pre-standard C++ or post 2017\n" ;
  return 0;
}