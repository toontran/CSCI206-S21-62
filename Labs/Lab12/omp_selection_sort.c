#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <omp.h>

/*
 * Students need to fill in the TODO places
 */

/*
 * The "merge()" function is adapted from
 * https://www.geeksforgeeks.org/merge-sort/
 *
 * Merges two subarrays of arr[].
 * First subarray is arr[l..m]
 * Second subarray is arr[m+1..r]
 */
 void merge(double arr[], int l, int m, int r)
 {
 	int i, j, k;
 	int n1 = m - l + 1;  		// number on left
 	int n2 = r - m;					// number on right

	// debug output
	printf("Merge %d %d %d (%d, %d)\n", l, m, r, n1, n2);

 	/* create temp arrays */
 	double *L = malloc(sizeof(double) * n1);
 	double *R = malloc(sizeof(double) * n2);

 	/* Copy data to temp arrays L[] and R[] */
 	memcpy(L, arr + l, n1 * sizeof(double));
 	memcpy(R, arr + m + 1, n2 * sizeof(double));

 	/* Merge the temp arrays back into arr[l..r]*/
 	i = 0; // Initial index of first subarray
 	j = 0; // Initial index of second subarray
 	k = l; // Initial index of merged subarray
 	while ((i < n1) && (j < n2))
 	{
 		if (L[i] <= R[j])
 			arr[k++] = L[i++];
 		else
 			arr[k++] = R[j++];
 	}

 	/* Copy the remaining elements of L[], if there	are any */
 	while (i < n1) arr[k++] = L[i++];
 	/* Copy the remaining elements of R[], if there are any */
 	while (j < n2) arr[k++] = R[j++];

 	free(L);
 	free(R);
 }

 // swap two locations (i,j) in the array
 void swap(double arr[], int i, int j) {
   double tmp = arr[i];
   arr[i] = arr[j];
   arr[j] = tmp;
 }

void selection_sort(double arr[], int size) {
  // TODO copy over from selection_sort.c, no changes needed.
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
	int blocksize;
    int i, current_sorted_blocks; // for merging
	double * a = NULL;            // the array of values
	
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
	printf("%s using %d threads on array of %d elements.\n",
		argv[0],
		NUM_THREADS,
		NUM_VALS);
	if (NUM_VALS % NUM_THREADS != 0){
		printf("ERROR: array size must be evenly divisible by the number of threads!\n");
		exit(254);
	}
	blocksize = NUM_VALS / NUM_THREADS;
	omp_set_num_threads(NUM_THREADS);     // request NUM_THREADS threads

	a = malloc(sizeof(double)*NUM_VALS);  // allocate memory for array
  fill_array(7891, a, NUM_VALS);        // initialize with random values

	printf("Generated array ");
  print_array(a, NUM_VALS);

	printf("Parallel sort\n");
  #pragma omp parallel                  // execute partial sorts in parallel
	{
		int ID = omp_get_thread_num();

    // TODO sort the ID'th block in the array
        printf("Sorting %d'th %d elenent block.\n", ID, blocksize);
        selection_sort(a + ID*blocksize, blocksize);
	}

	printf("Partially sorted array ");
  print_array(a, NUM_VALS);

	printf("Merge\n");
  // TODO Final merge operation on the sorted blocks.
  // this can be done sequentially or in parallel (maybe)
    current_sorted_blocks = NUM_THREADS;
    while (current_sorted_blocks > 1) {
        for (i=0; i<current_sorted_blocks; i+=2) {
            // Merge two blocks
            merge(a, blocksize * i, blocksize * (i+1) - 1, blocksize * (i+2) - 1);
        }
        current_sorted_blocks -= current_sorted_blocks / 2;    
        blocksize = blocksize * 2; // Each block is now double the size
    }

	printf("Sorted array is ");
  print_array(a, NUM_VALS);

	printf("Is sorted: %s\n",
		is_sorted(a, NUM_VALS) ? "YES": "NO -- FAILED");

  free(a);

  return 0;
}
