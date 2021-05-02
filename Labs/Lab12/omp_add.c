/*
 * https://www.openmp.org/wp-content/uploads/omp-hands-on-SC08.pdf
 * 2020-04-05
 * Downloaded for CSCI 206, spring 2020
 * with minor format revision
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <omp.h>

// array sum of n elements, nothing special here
double sum_array(double * a, int n)
{
  double sum = 0;
  while(n--){
    sum += *a++;
  }
  return sum;
}

// pseudo random array filler
void fill_array(int seed, double * a, int n)
{
  if (n == 16){
    // constant data if n == 16
    double d[16] = {4,4,4,4,7,7,7,7,1,1,1,1,5,5,5,5};
    memcpy(a, d, sizeof(double)*16);
    return;
  }
  srand(seed);
  while(n--){
    // rand returns an int between 0 and RAND_MAX, this maps it to [0...1]
    *a++ = (double)rand() / (double)RAND_MAX;
  }
}

// print an array of size n
void print_array(double * a, int n)
{
  int i;
  printf("[");
  for (i=0; i<n-1; i++){
    printf("%f, ", *a++);
    if (i > 15){
      //truncate array here
      printf("...]\n");
      return;
    }
  }
  printf("%f]\n", *a++);
}

int main(int argc, char * argv[])
{
  int i;                        // loop counter, etc
  int NUM_THREADS;              // how many threads to use
  int NUM_VALS;                 // how many values to sum
  double * a = NULL;            // the array of values
  double * par_sums = NULL;     // array to store partial results
  double sum;                   // the final sum
  double checkval;              // sequntial sum result (for verification)

  switch (argc){
    case 1:   // no arguments, use default values
      NUM_VALS = 16;
      NUM_THREADS = 4;
      break;
    case 2:   // just one argument, NUM_VALS
      NUM_VALS = atof(argv[1]);
      NUM_THREADS = 4;
      break;
    default:  // command line sets both values
      NUM_VALS = atof(argv[1]);
      NUM_THREADS = atof(argv[2]);
  }
  printf("omp_add using %d threads on array of %d elements.\n",
    NUM_THREADS,
    NUM_VALS);
  if (NUM_VALS % NUM_THREADS != 0){
    printf("ERROR: array size must be evenly divisible by the number of threads!\n");
    exit(254);
  }
  omp_set_num_threads(NUM_THREADS);     // request NUM_THREADS threads
  a = malloc(sizeof(double)*NUM_VALS);  // allocate memory for array
  par_sums = malloc(sizeof(double)*NUM_THREADS); // allocate partial sums
  fill_array(1234, a, NUM_VALS);        // initialize with random values
  printf("Input array: ");              // debug output
  print_array(a, NUM_VALS);

  #pragma omp parallel                  // execute partial adds in parallel
  {
    int ID = omp_get_thread_num();

    // each block processes NUM_VALS / NUM_THREADS values
    int blocksize = NUM_VALS / NUM_THREADS;

    // create partial sums

    // TODO call the sum_array on the block for this thread ID.
    // REPLACE the next line with a call to sum_array!
    par_sums[ID] = sum_array(a + ID * blocksize, blocksize);
//     par_sums[ID] = 0 / blocksize;
  }

  printf("partial_sums: ");             // debug output!
  print_array(par_sums, NUM_THREADS);

  // now reduce the partial sums to a single sum
  sum = 0;
  #pragma omp parallel for reduction(+: sum)
  for(i=0; i<NUM_THREADS; i++){
    sum += par_sums[i];
  }

  printf("sum = %f\n", sum);            // print the final sum

  // check the parallel sum by doing it in one shot
  checkval = sum_array(a, NUM_VALS);

  // becuase of the partial sums, there can be round off differences
  // betwen the results!
  if (fabs(sum - checkval) > NUM_VALS*1e-6){
    printf("ERROR sum is not correct\n");
    printf("The correct sum is %f\n", checkval);
    exit(255);
  }else{
    printf("Verified the sum.\n");
  }
  free(a);

  return 0;
}
