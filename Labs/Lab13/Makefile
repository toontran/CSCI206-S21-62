# on Hopper, we will benchmark you against Cray LibSci, the default vendor-tuned BLAS. The Cray compiler wrappers handle all the linking. If you wish to compare with other BLAS implementations, check the NERSC documentation.
# This makefile is intended for the GNU C compiler. On Hopper, the Portland compilers are default, so you must instruct the Cray compiler wrappers to switch to GNU: type "module swap PrgEnv-pgi PrgEnv-gnu"

CC = cc
CFLAGS = -Wall -Werror

# librt is needed for clock_gettime
LDLIBS = -lrt

targets = parse dm_cache_sim cache_sim benchmark-naive benchmark-blocked
objects = benchmark.o dgemm-naive.o dgemm-blocked.o

.PHONY : default
default : all

.PHONY : all
all : clean $(targets)

benchmark-naive : benchmark.o dgemm-naive.o
	$(CC) -o $@ $^ $(LDLIBS)
benchmark-blocked : benchmark.o dgemm-blocked.o
	$(CC) -o $@ $^ $(LDLIBS)

# math.h uses the math library, so link it on
cache_sim: cache_sim.o
	$(CC) -o $@ $^ -lm
dm_cache_sim: dm_cache_sim.o
	$(CC) -o $@ $^ -lm


.PHONY : clean
clean:
	rm -f $(targets) $(objects) *~ *.o
