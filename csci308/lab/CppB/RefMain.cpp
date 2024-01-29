#include<iostream>
#include"Ref.h"

using namespace std;


int main(){
  Ref obj1 = Ref();
  Ref obj2 = obj1;

  obj1.print();
  obj2.print();
  obj1.change(42);
  obj1.print();
  obj2.print();
}
