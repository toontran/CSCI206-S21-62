/*
 * CSCI 206 Computer Organization & Programming
 * Author: Alan Marchiori
 * Date: 2014-03-01
 * Updated for C: 2020-03-24
 * Copyright (c) 2014 Bucknell University
 *
 * Permission is hereby granted, free of charge, to any individual or
 * institution obtaining a copy of this software and associated
 * on files (the "Software"), to use, copy, modify, and
 * distribute without restriction, provided that this copyright and
 * permission notice is maintained, intact, in all copies and supporting
 * documentation.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL BUCKNELL UNIVERSITY BE LIABLE FOR ANY CLAIM, DAMAGES
 * OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
 * OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

#include <stdio.h>
#include <stdint.h>
#include <math.h>

float EPS = 0.00001;

float one_half_single(void){
  /*
  This function creates and returns a float with the value 0.5
  You cannot just "return 0.5;"!

  The 32-bit value 0x3f000000 is the value of 0.5 in IEEE 754.

  If we use an array to access the bytes, wwe have to return
  it in reverse order. Since the array is stored in little-endian
  byte order, the most significant bits of the float are in index [3]!
  +-------+-------+-------+-------+
  |  [0]  |  [1]  |  [2]  |  [3]  | Memory byte offset
  +-------+-------+-------+-------+
  |  7-0  |  15-8 | 23-16 | 31-24 | Bits (IEEE single)
  +-------+-------+-------+-------+
  */
  unsigned char val[4] = {0, 0, 0, 0x3f};
  return *(float*)val;
}

double one_half_double(void){
  /*
  Use an approach similar to one_half_single but now return
  the double precision IEEE 754 value for 0.5 (8 byte).
  */
  unsigned char val[8] = {0, 0, 0, 0, 0, 0, 0xe0, 0x3f};
  return *(double*)val;
}

unsigned f2u(float f){
  union {
    unsigned u;
    float f;
  } v;
  v.f = f;
  return v.u;
}

float u2f(unsigned d){
  union {
      unsigned u;
      float f;
  } v;
  v.u = d;
  return v.f;
}

unsigned long long d2u(double d){
  union {
    unsigned long long u;
    double d;
  } v;
  v.d = d;
  return v.u;
}

double u2d(unsigned long long u){
  union {
      unsigned long long u;
      double d;
  } v;
  v.u = u;
  return v.d;
}

void inspect_float(float f) {
    printf("Inspecting single %f, sign = %d, biased exponent = 0x%02x, fraction = 0x%06x\n", 
           f, !(f>0), (f2u(f) >> ((3 << 3) - 1)) & 0xFF, f2u(f) & 0x7FFFFF);
}

void inspect_double(double d) {
    printf("Inspecting double %lf, sign = %d, biased exponent = 0x%03llx, fraction = 0x%013llx\n", 
           d, !(d>0), (d2u(d) >>  ((6 << 3) + 4)) & 0xFFF, d2u(d) & 0xFFFFFFFFFFFFF);
}

float next_float(float f) {
    return u2f(f2u(f) + 1);
}

int is_near(float f1, float f2, float epsilon) {
    if (fabs(f1 - f2) < epsilon) return 1;
    else return 0;
}

int main()
{
  float a = 0.1;
  float sum = 0;
  int i;
  for (i = 0; i < 1000; i++)
  {
      sum += a;
  }

  printf ("a = %1.23f, sum = %1.23f, sum == 100 ==> %s\n",
          a,
          sum,
          is_near(sum, 100, 100*EPS) ? "TRUE":"FALSE");
    
  // It's not equal since the number 0.1 is not perfectly represented in floating point number
  // system: it contains error and the error gets larger as we accumulate the errors.

  inspect_float(a);
  inspect_float(sum);
  inspect_float(100-sum);
  return 0;
}


