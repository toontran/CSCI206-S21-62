#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{
  char * line = NULL;
  size_t len = 100;
  ssize_t read;
  char num[100];
  int i;

  if (argc != 2){
    printf("Usage: %s <trace file>\n", argv[0]);
    exit(1);
  }

  FILE* f = fopen(argv[1], "r");
  if (f==NULL){
    printf("Could not open file %s!\n", argv[1]);
    perror("fatal error");
    exit(-1);
  }

  int i_bytes = 0;    // I type access
  int s_bytes = 0;    // S and M type access
  int l_bytes = 0;    // L type access

  // TODO read file, parse each line, count bytes.
  while ((read = getline(&line, &len, f)) != -1) {
    for (i=2; i<(int)strlen(line); i++) {
      if (line[i] == ',') {
        strncpy(num, line + i + 1, strlen(line) - i - 1);          
        if (line[0] == 'I') i_bytes += atoi(num);
        else if (line[1] == 'S') s_bytes += atoi(num);
        else if (line[1] == 'L') l_bytes += atoi(num);
        else if (line[1] == 'M') s_bytes += atoi(num);
        else {
          printf("Can't parse: %s\n", line);
          break;
        }
      }
    }
  }

  // when done, print the results.
  printf("%d, %d, %d\n", i_bytes, l_bytes, s_bytes);
    
  fclose(f);
  if (line)
      free(line);
  return 0;
}
