// C++

#include <iostream>
#include <string>
using namespace std;

#include "friend.h"

// METHODS ARE CODED HERE
void RodeoClown::dance() { cout << "run away!.\n"; }
void RodeoClown::laugh() { cout << "haha.\n"; }
void RodeoClown::gallop() { cout << "giddyup\n"; }
void Bull::charge(RodeoClown * clown) {
  if (excited) clown->dance();
  else cout << "Moo Moo" << endl;
}
void Spectators::applaude(Bull * bull){ bull->excited = true;}

