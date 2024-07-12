#! /usr/bin/env python2

import os
import sys
import csv

list1 = os.path.abspath(sys.argv[1])
list2 = os.path.abspath(sys.argv[2])

with open(list1,'r') as csvfile:
    list1contents = [line.rstrip('\n') for line in csvfile.readlines()]

with open(list2,'r') as csvfile:
    list2contents = [line.rstrip('\n') for line in csvfile.readlines()]

set1 = set(list1contents)
set2 = set(list2contents)

set1_to_2_diff = set1 - set2
set2_to_1_diff = set2 - set1
intersection = set1 & set2

set1_string = os.path.basename(list1)
set2_string = os.path.basename(list2)

print(set1_string + ' - ' + set2_string + ' | count: ' + str(len(set1_to_2_diff)))
for line in list(sorted(set1_to_2_diff)):
    print(line)

print(set2_string + ' - ' + set1_string + ' | count: ' + str(len(set2_to_1_diff)))
for line in list(sorted(set2_to_1_diff)):
    print(line)

print(set1_string + ' & ' + set2_string + ' | count: ' + str(len(intersection)))
for line in list(sorted(intersection)):
    print(line)
