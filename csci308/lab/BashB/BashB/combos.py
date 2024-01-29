#!/usr/remote/anaconda-3.7-2020-08-12/bin/python
# Rob Barlow & Tung Tran

import itertools
import sys

output = []
#for i in sys.argv:
#	print(i)
for i in range(1,4):
	output.extend(list(itertools.combinations(sys.argv[1], i)))
for i in output:
	output_str = ''.join(i)
	print(output_str, end=' ')
print()
