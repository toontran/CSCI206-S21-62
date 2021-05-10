#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>


struct cache_line{
  int valid;
  long tag;
};


int main(int argc, char* argv[])
{
  if (argc < 3){
    printf("Usage: %s <cache size> <block size> <trace file>\n", argv[0]);
    printf("  all sizes are in bytes!\n");
    printf("  examples:\n");
    printf("    DM 4 kb with 8 byte blocks: %s 4096 8 <trace>\n", argv[0]);
    printf("    DM 16 kb with 16 byte blocks: %s 16384 16 <trace>\n", argv[0]);
    exit(1);
  }

  FILE* f = fopen(argv[3], "r");
  if (f == NULL){
    printf("Could not open file %s!\n", argv[3]);
    perror("fatal error");
    exit(-1);
  }

  int cache_size = atoi(argv[1]);
  int block_size = atoi(argv[2]);

  printf("Simulating a direct-mapped %d kb cache with %d byte blocks on trace %s.\n", cache_size >> 10, block_size, argv[3]);

  // count of total cache accesses and number of hits
  // count - hits = misses
  long count = 0;
  long hits = 0;

  // TODO process input file.
  // Allocate space for cache
  int i;
  int associativity = 1;
  int cache_lines = (cache_size / block_size) / associativity;
  struct cache_line *cache_struct = malloc(associativity*sizeof(struct cache_line)*cache_lines);
  for (i=0; i<cache_lines; i++) 
    cache_struct[i].valid = 0;
    
  // Read file, parse each line, count bytes.
  char * line = NULL;
  size_t len = 100;
  ssize_t read;
  char num[100];
  long tag;
  int tag_length = 8 - (int)log2(block_size) - (int)log2(cache_lines);
  while ((read = getline(&line, &len, f)) != -1) {
    if (line[1] == 'S') {
      strncpy(num, line + 3, 8);
      tag = (long)strtol(num, NULL, 16);
//       printf("%ld %ld\n", (tag >> (8-tag_length)), (tag/block_size)%cache_lines);
      if ( (tag >> (8-tag_length)) == cache_struct[(tag/block_size)%cache_lines].tag ) hits += 1;
      else {
        cache_struct[ (tag/block_size) % (cache_lines) ].tag = tag >> (8-tag_length);
        cache_struct[ (tag/block_size) % cache_lines ].valid = 1;
      }
      count += 1;
    }
  }
  
  

  // finally print results, do not change the last 3 lines of output.
  printf("  Hits      %ld\n", hits);
  printf("  Misses    %ld\n", count-hits);
  printf("  Miss rate %f\n", (double)(count-hits)/(double)count);

  return 0;
}
