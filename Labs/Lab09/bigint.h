#ifndef bigint_h_
#define bigint_h_

struct bigint {
  int N;
  char digit[];
};

// INIT, create a bigint with value (given in binary)
struct bigint*  bigint_init(char* value, int N);

// set the value to zero
void bigint_zero(struct bigint* bn);

// OUTPUT a bigint to a pre-allocated C string
void bigint_str(char* dst, struct bigint* bn);

// needed for extra credit
void bigint_hexstr(char* dst, struct bigint* bn);
struct bigint* bigint_copy(struct bigint* in);

// BITWISE OPERATIONS
void bigint_inv(struct bigint* out, struct bigint* in);
void bigint_rshift(struct bigint *bn, int bits);
void bigint_lshift(struct bigint *bn, int bits);

// LOGICAL operations
int bigint_iszero(struct bigint* in);

// ARITHMETIC
void bigint_add(struct bigint* c, struct bigint* a, struct bigint* b);
void bigint_sub(struct bigint* c, struct bigint* a, struct bigint* b);
void bigint_mult(
  struct bigint* prod,
  struct bigint* mcand,
  struct bigint* mplier);

void bigint_div(
  struct bigint* quotient,
  struct bigint* remainder,
  struct bigint* dividend,
  struct bigint* divisor);

void bigint_fact(
  struct bigint* result,
  struct bigint* in);

#endif
