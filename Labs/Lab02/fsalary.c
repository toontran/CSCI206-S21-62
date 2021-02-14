/* Tung Tran
 * date/ 1:20 - 3:10
 * lab 02 - salary.c
 * compile with: make salary
 * notes: none
 */
#include <stdio.h>
 
int main(void) 
{
    float hourly_wage;
    int weeks_worked;

    printf("Enter hourly wage (float): "); scanf("%f", &hourly_wage);
    printf("Enter weeks worked (integer): "); scanf("%d", &weeks_worked);
 
    printf("Annual salary is: ");
    printf("%.2f", hourly_wage * 40 * weeks_worked);
    printf("\n");
 
    return 0;
}

