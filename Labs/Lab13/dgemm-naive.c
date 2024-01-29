const char* dgemm_desc = "Naive, three-loop dgemm.";

/* This routine performs a dgemm operation
 *  C := C + A * B
 * where A, B, and C are n-by-n matrices stored in column-major format.
 * On exit, A and B maintain their input values.
 */    
void square_dgemm (int n, double* A, double* B, double* C)
{
  int i,j,k;
  /* For each row i of A */
  for (i = 0; i < n; ++i)
    /* For each column j of B */
    for (j = 0; j < n; ++j) 
    {
      /* Compute C(i,j) */
      double cij = C[i+j*n];
      for(k = 0; k < n; k++ )
        cij += A[i+k*n] * B[k+j*n];
      C[i+j*n] = cij;
    }
}
