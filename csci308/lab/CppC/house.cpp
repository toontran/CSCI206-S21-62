#include<iostream>
using namespace std;

class House{
public:
  int number;

  House() = default; // Default constructor
  House(int i);
};

House::House(int i){ this->number = i; }

ostream & operator<<(ostream &c, House h){
  c << "   _   " << endl;
  c << "  / \\  " << endl;
  c << " /   \\ " << endl;
  c << " ----- " << endl;
  c << " | " << h.number << " | " << endl;
  c << " ----- " << endl;
  return c;
}

int main(){
  House h = House(8);
  House h1 = House(5);
  
  cout << h << h1 << endl;
  return 0;
}
