#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "stack.h"



int is_operator(char* token){
    if (strcmp(token, "+") == 0) return 1;
    else if (strcmp(token, "-") == 0) return 1;
    else if (strcmp(token, "x") == 0) return 1;
    else if (strcmp(token, "/") == 0) return 1;
    else if (strcmp(token, "^") == 0) return 1;
    else return 0;
}

float evaluate(char* operator, float *operand_1, float *operand_2) {
    if (strcmp(operator, "+") == 0) return *operand_1 + *operand_2;
    else if (strcmp(operator, "-") == 0) return *operand_1 - *operand_2;
    else if (strcmp(operator, "x") == 0) return *operand_1 * (*operand_2);
    else if (strcmp(operator, "^") == 0) return pow(*operand_1, *operand_2);
    else return *operand_1 / *operand_2;
}

int main(int argc, char* argv[]) 
{
    int i;
    struct stack* stack = stack_create();
    float operand_1, operand_2;
    float result;

    if ((argc < 1)) {
        printf("Usage: ./pcalc <arguments..>\n");
        return 0;
    }
    
    for (i=1; i < argc; i++) {
        if (is_operator(argv[i]) == 1) {
            stack_pop(stack, &operand_2, sizeof(float));
            stack_pop(stack, &operand_1, sizeof(float));
            result = evaluate(argv[i], &operand_1, &operand_2);
            stack_push(stack, &result, sizeof(float));
        } else {
            result = atof(argv[i]);
            stack_push(stack, &result, sizeof(float));//if (is_operand(argv[i]))
        }
    }
    
    while (!stack_empty(stack)){
        stack_pop(stack, &result, sizeof(float));
        printf("%f\n", result);
    }

    stack_destroy(stack);
    return 0;
}
