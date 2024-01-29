#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "bigint.h"


struct bigint* bigint_init(char* value, int N){
  int i;
  int k = strlen(value);
  struct bigint* r;

  // ensure N is divisible by 4
  if (N%4 > 0){
    N += (4-(N%4));
  }

  if (k > N){
    printf("ERROR: too many digits\n");
    exit(1);
  }

  r = malloc(sizeof(struct bigint) + N);
  r->N = N;
  bigint_zero(r);

  // copy digits from the C string value into the digits
  for(i = 0; i < k; i++){
    r->digit[k-i-1] = value[i];
  }
  return r;
}

void bigint_zero(struct bigint* bn){
  memset(bn->digit, '0', bn->N);
}

void bigint_str(char* dst, struct bigint* bn){
  int i;
  for(i = bn->N; i > 0; i--){
    *dst++ = bn->digit[i-1];
    if ( (i-1)%4 == 0){
      *dst++ = ' ';
    }
  }
  *dst = '\0';
}

void bigint_hexstr(char* dst, struct bigint* bn){
  int i;
  int is_trailing_zeros = 1;
  int sum;
  for(i = bn->N/4; i > 0; i--){    
    // Sum a block of 4 bits
    sum = 0;
    if (bn->digit[i*4-1] == '1') sum += 8;
    if (bn->digit[i*4-2] == '1') sum += 4;
    if (bn->digit[i*4-3] == '1') sum += 2;
    if (bn->digit[i*4-4] == '1') sum += 1;
      
    // For numbers greater or equal 9
    if (sum != 0) is_trailing_zeros = 0;
      
    if (sum == 10) *dst++ = 'a';
    else if (sum == 11) *dst++ = 'b';
    else if (sum == 12) *dst++ = 'c';
    else if (sum == 13) *dst++ = 'd';
    else if (sum == 14) *dst++ = 'e';
    else if (sum == 15) *dst++ = 'f';
    else if (sum == 0 && is_trailing_zeros);
    else {
        *dst++ = sum+'0';
    }
  }
  *dst= '\0';
}

// this IS useful
void full_add(char carry_in, char a, char b, char* sum, char* carry_out){
  int i =0;
  if (a == '1') i++;
  if (b == '1') i++;
  if (carry_in == '1') i++;
  switch(i){
    case 0: *sum = '0'; *carry_out = '0'; break;
    case 1: *sum = '1'; *carry_out = '0'; break;
    case 2: *sum = '0'; *carry_out = '1'; break;
    case 3: *sum = '1'; *carry_out = '1'; break;
    default: printf("Impossible error!\n"); exit(255);
  }
}

void bigint_add(struct bigint* c, struct bigint* a, struct bigint* b){
  int i;
  char carry_out = '0';
  for (i=0; i<c->N; i++) {
    full_add(carry_out, a->digit[i], b->digit[i], &c->digit[i], &carry_out);
  }
  if ((c->digit[c->N-1] == '1' && a->digit[c->N-1] == '0' && b->digit[c->N-1] == '0')
      || (c->digit[c->N-1] == '1' && a->digit[c->N-1] == '0' && b->digit[c->N-1] == '0')) {
    printf("Overflow error!\n"); exit(255);
  }
}

void bigint_inv(struct bigint* out, struct bigint* in){
  struct bigint *temp;
  int i;
  if (in->digit[in->N-1] == '0') {
      for (i=0; i<out->N; i++) {
          if (in->digit[i] == '0') out->digit[i] = '1';
          else out->digit[i] = '0';
      }
      temp = bigint_init("1", out->N);
      bigint_add(out, out, temp);
  }
  free(temp);
}

void bigint_sub(struct bigint* c, struct bigint* a, struct bigint* b){
  bigint_inv(c, b);
  bigint_add(c, a, c);
}

void bigint_rshift(struct bigint *bn, int bits){
  char s[bn->N];
  int i;
  for (i=0; i<bn->N-bits; i++) {
    s[i] = bn->digit[i+bits];
  }
  for (i=bn->N-bits; i<bn->N; i++) {
    s[i] = '0';
  }
  for (i=0; i<bn->N; i++) {
    bn->digit[i] = s[i];
  }
}

void bigint_lshift(struct bigint *bn, int bits){
  char s[bn->N];
  int i;
  for (i=bits; i<bn->N; i++) {
    s[i] = bn->digit[i-bits];
  }
  for (i=0; i<bits; i++) {
    s[i] = '0';
  }
  for (i=0; i<bn->N; i++) {
    bn->digit[i] = s[i];
  }
}

void bigint_mult(
  struct bigint* prod,
  struct bigint* mcand,
  struct bigint* mplier){
  // Unoptimized multiplication
  int i;
  for (i=0; i<prod->N; i++){
      if (mplier->digit[i] == '1')
          bigint_add(prod, prod, mcand);
      bigint_lshift(mcand,1);
  }
}

void bigint_div(
  struct bigint* quotient,
  struct bigint* remainder,
  struct bigint* dividend,
  struct bigint* divisor){
  // Unoptimized division
  int i;
  struct bigint* temp = bigint_init("", remainder->N);
    
  // Initialize divisor in top half of register.
  for (i=0; i<divisor->N/2; i++){  
    divisor->digit[i + divisor->N/2] = divisor->digit[i];
  }
  for (i=0; i<divisor->N/2; i++){
    divisor->digit[i] = '0';
  }

  // copy values from dividend into remainder 
  strcpy(remainder->digit, dividend->digit);
    
  // The loop
  for (i=0; i<divisor->N/2+1; i++){
    strcpy(temp->digit, remainder->digit);
    bigint_sub(temp, remainder, divisor);
    bigint_lshift(quotient, 1);
    if (temp->digit[remainder->N-1] == '1') {
      quotient->digit[i] = '0';
    } else {
      strcpy(remainder->digit, temp->digit);
      quotient->digit[0] = '1';
    }
    bigint_rshift(divisor, 1);
  }
  free(temp);
}
int bigint_iszero(struct bigint* in){
  int i;
  for (i=0; i<in->N; i++) {
      if(in->digit[i] == '1') return 0;
  }
  return 1;
}
struct bigint* bigint_copy(struct bigint* in){
  return in;
}
void bigint_fact(
  struct bigint* result,
  struct bigint* in){
    
  struct bigint* number_one = bigint_init("1", result->N);
  struct bigint* temp = bigint_init("", result->N);
  struct bigint* temp2 = bigint_init("1", result->N);
  struct bigint* temp3 = bigint_init("", result->N);
//   char a_str[result->N*2];
  
  strcpy(result->digit, number_one->digit); // result = 1
    
  while (!bigint_iszero(temp2)) {
    bigint_add(temp, temp, number_one); // temp += 1
    strcpy(temp2->digit, result->digit);
    // Multiply
    bigint_mult(temp3, temp2, temp);
    strcpy(result->digit, temp3->digit);
    // Reset temp3=0 for next multiplication
    bigint_sub(temp3, number_one, number_one); 
    // temp2 = temp - result
    bigint_sub(temp2, temp, in);
//     bigint_str(a_str, result);
//     printf("%s\n", a_str);
  }
  free(temp);
  free(number_one);
  free(temp2);
}
