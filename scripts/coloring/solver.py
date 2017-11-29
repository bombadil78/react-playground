#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from subprocess import Popen, PIPE

def solve_it(input_data):
    tmp_file_name = 'tmp.data'
    tmp_file = open(tmp_file_name, 'w')
    tmp_file.write(input_data)
    tmp_file.close()

    process = Popen(['java', '-cp', '/home/christoph/code/discrete-optimization/target/do-0.1.jar', 'ch.bullsoft.coloring.Coloring', '-file=' + tmp_file_name], stdout=PIPE)
    (stdout, stderr) = process.communicate()

    os.remove(tmp_file_name)
    return stdout.strip()


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
