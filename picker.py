import sys
import re
desired_samples = open(sys.argv[1])
input_str = open(sys.argv[2])
output_file = sys.argv[3]
sample_list = desired_samples.readlines()
stru = input_str.readlines()
new_lines = []

for line in stru:
        found = line.split('.')
        strf = int(found[0])
        for x in sample_list:
		if int(x) == strf:
			print 'match'
                	new_lines.append(line)
print new_lines
with open(output_file, 'w') as f:
       [f.write(line) for line in new_lines]
