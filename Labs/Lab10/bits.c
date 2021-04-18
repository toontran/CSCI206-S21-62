/*
 * CSCI 206 Computer Organization & Programming
 * Author: Alan Marchiori
 * Date: 2014-02-28
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

#if 0
/*
 * Instructions to Students:
 *
 * STEP 1: Read the following instructions carefully.
 */

You will develop your solution by
editing the collection of functions in this source file.

INTEGER CODING RULES:

  Replace the "return 2" statement in each function with one
  or more lines of C code that implements the function. Your code
  must conform to the following style:

  int Funct(arg1, arg2, ...) {
      /* brief description of how your implementation works */
      int var1 = Expr1;
      ...
      int varM = ExprM;

      varJ = ExprJ;
      ...
      varN = ExprN;
      return ExprR;
  }

  Each "Expr" is an expression using ONLY the following:
  1. Integer constants 0 through 255 (0xFF), inclusive. You are
      not allowed to use big constants such as 0xffffffff.
  2. Function arguments and local variables (no global variables).
  3. Unary integer operations ! ~
  4. Binary integer operations & ^ | + << >>

  Some of the problems restrict the set of allowed operators even further.
  Each "Expr" may consist of multiple operators. You are not restricted to
  one operator per line.

  You are expressly forbidden to:
  1. Use any control constructs such as if, do, while, for, switch, etc.
  2. Define or use any macros.
  3. Define any additional functions in this file.
  4. Call any functions.
  5. Use any other operations, such as &&, ||, -, or ?:
  6. Use any form of casting.
  7. Use any data type other than int.  This implies that you
     cannot use arrays, structs, or unions.


  You may assume that your machine:
  1. Uses 2s complement, 32-bit representations of integers.
  2. Performs right shifts arithmetically.
  3. Has unpredictable behavior when shifting an integer by more
     than the word size.

EXAMPLES OF ACCEPTABLE CODING STYLE:
  /*
   * pow2plus1 - returns 2^x + 1, where 0 <= x <= 31
   */
  int pow2plus1(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     return (1 << x) + 1;
  }

  /*
   * pow2plus4 - returns 2^x + 4, where 0 <= x <= 31
   */
  int pow2plus4(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     int result = (1 << x);
     result += 4;
     return result;
  }
#endif

#include <stdio.h>
#include <stdlib.h>

/*==================== EXERCISE 1: get_byte ====================
 * get_byte - Extract byte n from word x
 * example: get_byte(0x12345678, 1) = 0x56
 * legal ops: ~ ! & ^ | + << >>
 */
int get_byte(int x, int n)
{
    return (int) (unsigned) x >> (n << 3) & 0xFF;
}

/* baseline implementation of get_byte
 * this uses illegal ops
 * DO NOT MODIFY THIS FUNCTION
 */
int baseline_get_byte(int x, int n)
{
    unsigned char byte;
    switch(n) {
    case 0:
        byte = x;break;
    case 1:
        byte = x >> 8;
        break;
    case 2:
        byte = x >> 16;
        break;
    default:
        byte = x >> 24;
        break;
    }
    return (int) (unsigned) byte;
}

/*
 * test script for get_byte
 * DO NOT MODIFY THIS FUNCTION
 */
void test_get_byte(void)
{
    int inputs[] = {0x12345678, 0xdeadbeef, 0xfeedf00d};
    int n;
    int input;
    for (input = 0; input < sizeof(inputs)/sizeof(inputs[0]); input++){
        for (n = 0; n < 4; n++){
            int a = get_byte(inputs[input], n);
            int b = baseline_get_byte(inputs[input], n);

            printf("get_byte(0x%08x, %d): returned 0x%02x, wanted 0x%02x ===> %s\n",
                    inputs[input],
                    n,
                    a,
                    b,
                    a == b ? "PASS":"FAIL" );
        }
    }
}


/*==================== EXERCISE 2: negate ====================
 *
 * returns the negation of a two's complement integer
 * by manipulating the data at the bit-level. do not
 * use the - operator!
 * Example: negate(1) = -1
 * Legal ops: ! ~ & ^ | + >> <<
 */
int negate(int x)
{
    return (int) (unsigned)  ~(x + ((~1+1) & x >> 31)) + !(x >> 31);
}

/* baseline implementation of negate
 * this uses illegal ops
 * DO NOT MODIFY THIS FUNCTION
 */
int baseline_negate(int x)
{
    return -x;
}

/*
 * test script for negate
 * DO NOT MODIFY THIS FUNCTION
 */
void test_negate(void)
{
    int inputs[] = {1, 20, -42, -32768};
    int input;
    for (input = 0; input < sizeof(inputs)/sizeof(inputs[0]); input++){
        int a = negate(inputs[input]);
        int b = baseline_negate(inputs[input]);

        printf("negate(%6d): returned %6d, wanted %6d ===> %s\n",
                inputs[input],
                a,
                b,
                a == b ? "PASS":"FAIL" );
    }

}

/*==================== EXERCISE 3: is_positive ====================
 *
 * returns 1 if the number is > 0
 * Example: is_positive(-1) = 0.
 * Lgal ops: ! ~ & ^ | + << >>
 */
int is_positive(int x)
{
    return !((x+(~1+1)) >> 31);
}

/* baseline implementation of is_positive
 * this uses illegal ops
 * DO NOT MODIFY THIS FUNCTION
 */
int baseline_is_positive(int x)
{
    return x > 0;
}

/*
 * test script for is_positive
 * DO NOT MODIFY THIS FUNCTION
 */
void test_is_positive(void)
{
    int inputs[] = {1, 0, -42, -32768};
    int input;
    for (input = 0; input < sizeof(inputs)/sizeof(inputs[0]); input++){
        int a = is_positive(inputs[input]);
        int b = baseline_is_positive(inputs[input]);

        printf("is_positive(%6d): returned %6d, wanted %6d ===> %s\n",
                inputs[input],
                a,
                b,
                a == b ? "PASS":"FAIL" );
    }

}


/* ==================== tmax / tmin ====================
 *
 * tmax(n) - return the maximum (largest) two's complement integer
 *   using up to n bits (assume n = [2..32])
 * legal ops: ~ ! & ^ | + - >> <<
 */
int tmax(int n)
{
    return 0xFFFFFFFF >> (32+(~n+2));
}

/* baseline implementation of tmax
 * this uses illegal ops
 * DO NOT MODIFY THIS FUNCTION
 */
int baseline_tmax(int n)
{
    // the max 2's complelment integer is 2^(n-1) - 1
    // the for loop comptues 2^(n-1)
    // then we subtract one
    int x = 1;
    int i;
    for (i=1; i < n; i++)
        x *= 2;
    x -= 1;
    return x;
}

/* tmin(n) - return the minimum (smallest) two's complement integer
 *   using up to n bits (assume n = [2..32])
 * legal ops: ~ ! & ^ | + - >> <<
 */
int tmin(int n)
{
    return 0xFFFFFFFF << (n+(~1+1));
}

/* baseline implementation of tmin
 * this uses illegal ops
 * DO NOT MODIFY THIS FUNCTION
 */
int baseline_tmin(int n)
{
    int x = -1;
    int i;
    for (i=1; i < n; i++)
        x *= 2;
    return x;
}

/*
 * test script for tmax and tmin
 * DO NOT MODIFY THIS FUNCTION
 */
void test_tmax_tmin(void)
{
    int n;
    for (n = 2; n <= 32; n++){
        int a = tmax(n);
        int b = baseline_tmax(n);
        printf ("tmax(%d): returned 0x%08x, wanted 0x%08x ===> %s\n",
                n,
                a,
                b,
                a == b ? "PASS":"FAIL");
        a = tmin(n);
        b = baseline_tmin(n);
        printf ("tmin(%d): returned 0x%08x, wanted 0x%08x ===> %s\n",
            n,
            a,
            b,
            a == b ? "PASS":"FAIL");

    }
}

/*==================== main ====================
 * DO NOT MODIFY THIS FUNCTION
 */
int main(int argc, char* argv[])
{
  int test = 99;
  if (argc > 1){
    test = atoi(argv[1]);
  }
  if (test > 0)
    test_get_byte();
  if (test > 1)
    test_negate();
  if (test > 2)
    test_is_positive();
  if (test > 3)
    test_tmax_tmin();

  return 0;
}
