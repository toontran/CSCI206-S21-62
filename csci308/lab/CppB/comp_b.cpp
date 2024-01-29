#include<iostream>
#include "comp_a.h"

using namespace std;
void reinit(){
  global_var = 0;
}

void print(){
  cout << "global_var = " << global_var << endl;
}

