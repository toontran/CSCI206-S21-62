#include<iostream>

// Ref class
// public bool mybool
// private in myint
// public print() and change()

using namespace std;
class Ref {
public:
  bool mybool;
  Ref();
  void print();
  void change(int i);

private:
  int myint;
};

// mybool = 1
// myint = 8


Ref::Ref() {
  this->mybool = true;
  this->myint = 8;
}

void Ref::print() {
  cout << this->mybool << ' ' << this->myint << endl;
}

void Ref::change(int i) {
  this->myint = i;
}
