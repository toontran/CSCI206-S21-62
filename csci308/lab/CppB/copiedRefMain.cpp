#include<iostream>
#include"Ref.cpp"
using namespace std;


int main(){
  Ref obj1 = Ref();
  Ref obj2 = obj1;

  obj1.print();
  obj2.print();
}
