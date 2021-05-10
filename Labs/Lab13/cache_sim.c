#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>


struct cache_line{
  int valid;
  long tag;
  int turns_left; // 0 turns left means the oldest cache line when associativity > 1
};


int main(int argc, char* argv[])
{
  if (argc < 4){
    printf("Usage: %s <cache size> <block size> <associativity> <trace file>\n", argv[0]);
    printf("  all sizes are in bytes!\n");
    printf("  examples:\n");
    printf("    DM 4 kb with 8 byte blocks: %s 4096 8 1 <trace>\n", argv[0]);
    printf("    DM 16 kb with 16 byte blocks: %s 16384 16 1 <trace>\n", argv[0]);
    printf("    4-way 16 kb with 16 byte blocks: %s 16384 16 4 <trace>\n", argv[0]);
    exit(1);
  }

  FILE* f = fopen(argv[4], "r");
  if (f == NULL){
    printf("Could not open file %s!\n", argv[4]);
    perror("fatal error");
    exit(-1);
  }

  int cache_size = atoi(argv[1]);
  int block_size = atoi(argv[2]);
  int associativity = atoi(argv[3]);
  printf("Simulating %d-way associative %d kb cache with %d byte blocks on trace %s.\n",
    associativity, cache_size >> 10, block_size, argv[4]);

  // count of total cache accesses and number of hits
  // count - hits = misses
  long count = 0;
  long hits = 0;

  // TODO process input file.
  // Allocate space for cache
  int i;
  int cache_lines = (cache_size / block_size) / associativity;
  if (cache_lines == 0) cache_lines = 1;
  struct cache_line *cache_struct = malloc(associativity*sizeof(struct cache_line)*cache_lines);
  for (i=0; i<cache_lines*associativity; i++) {
    cache_struct[i].valid = 0;
    cache_struct[i].turns_left = 0;
  }
  // Read file, parse each line, count bytes.
  char * line = NULL;
  size_t len = 100;
  ssize_t read;
  char num[100];
  long tag;
  int tag_length = 8 - (int)log2(block_size) - (int)log2(cache_lines);
  int need_override;
  while ((read = getline(&line, &len, f)) != -1) {
    if (line[0] == 'S') {
      strncpy(num, line + 3, 8);
      tag = (long)strtol(num, NULL, 16);
      need_override = 1;
//       printf("%ld %ld %ld\n", tag, (tag >> (8-tag_length)), (tag/block_size)%cache_lines);
      for (i=0; i<associativity; i++) {
        if ( (tag >> (8-tag_length)) == cache_struct[((tag/block_size)%cache_lines) * associativity + i].tag ) {
          hits += 1;
          need_override = 0;
//           printf("HIT: %ld %ld %ld %d\n", (tag >> (8-tag_length)), ((tag/block_size)%cache_lines) * associativity + i, (tag/block_size)%cache_lines, i);
          break;
        }
      }
      
      if (need_override) {
        for (i=0; i<associativity; i++) {
          if (cache_struct[((tag/block_size)%cache_lines) * associativity + i].turns_left == 0 && need_override) {
            cache_struct[ ((tag/block_size)%cache_lines) * associativity + i ].tag = tag >> (8-tag_length);
            cache_struct[ ((tag/block_size)%cache_lines) * associativity + i ].valid = 1;
            cache_struct[ ((tag/block_size)%cache_lines) * associativity + i ].turns_left = associativity;
            need_override = 0;
//             printf("MISS: %ld %ld %ld %d\n", (tag >> (8-tag_length)), ((tag/block_size)%cache_lines) * associativity + i, (tag/block_size)%cache_lines, i);
          }
          if (cache_struct[((tag/block_size)%cache_lines) * associativity + i].turns_left != 0)
            cache_struct[ ((tag/block_size)%cache_lines) * associativity + i ].turns_left -= 1;
        }
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
