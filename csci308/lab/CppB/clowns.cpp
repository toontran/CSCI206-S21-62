#include<iostream>

using namespace std;
class Clown {
public:
  Clown(){}
  string name;
  Clown(string name) { this->name = name; }
  virtual void dance() { cout << this->name << " twirls like a ballerina" << endl; }
};

class CircusClown: public Clown {
public:  
  CircusClown(string name) { this->name = name; }
  void dance() { cout << this->name <<  " hops up and down" << endl; }
};

int main() {
  Clown* carl = new Clown("Carl");
  carl->dance();

  CircusClown* joe = new CircusClown("Joe");
  joe->dance();
  
  Clown* bob = new CircusClown("Bob");
  bob->dance();

  Clown* joeJr = (Clown*) joe;
  joeJr->dance();
}

