/*
 * https://www.openmp.org/wp-content/uploads/omp-hands-on-SC08.pdf
 * 2020-04-05
 * Downloaded for CSCI 206, spring 2020
 * with minor format revision
 */
#include <stdio.h>
#include <omp.h>
int main(int argc, char * argv[])
{
#pragma omp parallel
  {
	int ID = omp_get_thread_num();
	printf(" hello(%d) ", ID);
	printf(" world(%d) \n", ID);
  }

  printf("We are all done with parallel!\n");

  return 0;
}
