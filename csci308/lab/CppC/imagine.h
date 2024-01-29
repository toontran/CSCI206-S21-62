#ifndef IMAGINE_H
#define IMAGINE_H

#include<iostream>
using std::ostream;

class Imag{
public:
  double real;
  double imag;

  /* This constructor gets written for you automatically. */
  Imag() = default;

  /* You get to write this constructor. */
  Imag(double,double);

  /* add is a method that the first imag calls on the second imag. It returns
     a third Imag with the answer without modifying the first or second Imags. */
  Imag add(Imag);

  /* mult is a method that the first imag calls on the second imag. It returns
     a third Imag with the answer without modifying the first or second Imags. */
  Imag mult(Imag);
};

/* The + operator needs to declare and return an Imag (not n1 or n2). 
   This Imag is the result of calling the add() method above. */
Imag operator+(Imag n1, Imag n2);

/* The * operator needs to declare and return an Imag (not n1 or n2) 
   This Imag is the result of calling the mult() method above. */
Imag operator*(Imag n1, Imag n2);

/* The << operator prints the Imag to the ostream c (it might not always be cout). */
ostream & operator<<(ostream &c, Imag n);

#endif
