#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
/*
 * Students need to fill in the TODO places
 */

// swap two locations (i,j) in the array
void swap(double arr[], int i, int j) {
  double tmp = arr[i];
  arr[i] = arr[j];
  arr[j] = tmp;
}

void selection_sort(double arr[], int size) {
	// TODO write selection sort.
    int min_location, i, current_min_idx;
    double current_min;
    
    for (min_location=0; min_location < size; min_location++) {
        current_min = arr[min_location];
        current_min_idx = min_location;
        // Find smallest element
        for (i=min_location+1; i < size; i++) {
            if (arr[i] < current_min) {
                current_min = arr[i];
                current_min_idx = i;
            }
        }
        // Swap
        arr[current_min_idx] = arr[min_location];
        arr[min_location] = current_min;
    }
}

/* UTILITY FUNCTIONS */
// print an array of size n
void print_array(double * a, int n){
  int i;
	if(n <= 16){
		// print the whole thing
		printf("[");
		for (i=0; i<n-1; i++){
	    printf("%f, ", a[i]);
		}
		printf("%f]\n", a[i]);
	} else {
		// truncate the printout
	  printf("[");
		// print first 8
	  for (i=0; i<8; i++){
	    printf("%f, ", a[i]);
	  }
		printf("..., ");
		// print last 8
		for (i=n-9; i < n-1; i++){
			printf("%f, ", a[i]);
		}
	  printf("%f]\n", a[i]);
	}
}

// pseudo random array filler
void fill_array(int seed, double * a, int n){
  if (n == 16){
    // constant data if n == 16
    const double d[16] = {4,4,4,4,7,7,7,7,1,1,1,1,5,5,5,5};
    memcpy(a, d, sizeof(double)*16);
    return;
  }
  srand(seed);
  while(n--){
    // rand returns an int between 0 and RAND_MAX, this maps it to [0...1]
    *a++ = (double)rand() / (double)RAND_MAX;
  }
}

// check if an array is sorted, return 1 if true, 0 if not.
int is_sorted(double arr[], int n){
	int i;
	// check for any out of order elements
	for (i=0; i<n-1; i++){
		if (arr[i] > arr[i+1])
			return 0;
	}
	return 1;
}

/* Driver program to test above functions */
int main(int argc, char *argv[])  {
	int NUM_THREADS;              // how many threads to use
	int NUM_VALS;                 // how many values to sum
	double * a = NULL;            // the array of values

	switch (argc){
		case 1:   // no arguments, use default values
			NUM_VALS = 16;
			NUM_THREADS = 1;
			break;
		case 2:   // just one argument, NUM_VALS
			NUM_VALS = atof(argv[1]);
			NUM_THREADS = 1;
			break;
		default:  // command line sets both values
			NUM_VALS = atof(argv[1]);
			NUM_THREADS = 1;
	}
	printf("%s using %d threads on array of %d elements.\n",
		argv[0],
		NUM_THREADS,
		NUM_VALS);
	if (NUM_VALS % NUM_THREADS != 0){
		printf("ERROR: array size must be evenly divisible by the number of threads!\n");
		exit(254);
	}

  a = malloc(sizeof(double)*NUM_VALS);  // allocate memory for array
  fill_array(7891, a, NUM_VALS);        // initialize with random values

  printf("Generated array ");
  print_array(a, NUM_VALS);

	printf("Sorting. . .\n");
  selection_sort(a, NUM_VALS);

  printf("Sorted array is ");
  print_array(a, NUM_VALS);

	printf("Is sorted: %s\n",
		is_sorted(a, NUM_VALS) ? "YES": "NO -- FAILED");

  free(a);

  return 0;
}
