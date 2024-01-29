#include <iostream>
#include "imagine.h"

using namespace std;

Imag::Imag(double r, double i) {
    this->real = r;
    this->imag = i;
} 

Imag operator+ (Imag i1, Imag i2) {
    return Imag(i1.real+i2.real, i1.imag+i2.imag);
}

Imag operator* (Imag i1, Imag i2) {
    return Imag((i1.real*i2.real) - (i1.imag*i2.imag), 
                (i1.real*i2.imag) + (i1.imag*i2.real));
}

ostream & operator<< (ostream &c, Imag i) {
    c << i.real << " + i" << i.imag;
    return c;
}
