#include<iostream>

using namespace std;
class A {
public:
  virtual void f() { cout << "Method from A" << endl; }
  void g() { this->f(); }
};

class B: public A {
  void f() { cout << "Method from B" << endl; }
};

int main() {
  B b;
  b.g();
}

