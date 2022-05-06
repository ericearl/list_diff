#! /usr/bin/env python2

import os
import sys
import csv

list1 = os.path.abspath(sys.argv[1])
list2 = os.path.abspath(sys.argv[2])
list3 = os.path.abspath(sys.argv[3])

with open(list1,'rb') as csvfile:
    list1contents = [line.rstrip('\n') for line in csvfile.readlines()]

with open(list2,'rb') as csvfile:
    list2contents = [line.rstrip('\n') for line in csvfile.readlines()]

with open(list3,'rb') as csvfile:
    list3contents = [line.rstrip('\n') for line in csvfile.readlines()]

set1 = set(list1contents)
set2 = set(list2contents)
set3 = set(list3contents)

intersect_all = set1 & set2 & set3
intersect_1_2 = set1 & set2 - set3
intersect_1_3 = set1 & set3 - set2
intersect_2_3 = set2 & set3 - set1
set1_only     = set1 - set2 - set3
set2_only     = set2 - set1 - set3
set3_only     = set3 - set1 - set2

set1s = os.path.basename(list1)
set2s = os.path.basename(list2)
set3s = os.path.basename(list3)

intersect_alls = '%s & %s & %s' % (set1s,set2s,set3s)
intersect_1_2s = '%s & %s - %s' % (set1s,set2s,set3s)
intersect_1_3s = '%s & %s - %s' % (set1s,set3s,set2s)
intersect_2_3s = '%s & %s - %s' % (set2s,set3s,set1s)
set1_onlys     = '%s - %s - %s' % (set1s,set2s,set3s)
set2_onlys     = '%s - %s - %s' % (set2s,set1s,set3s)
set3_onlys     = '%s - %s - %s' % (set3s,set1s,set2s)

print(set1_onlys + ' | count: ' + str(len(set1_only)))
for line in list(sorted(set1_only)):
    print(line)

print(set2_onlys + ' | count: ' + str(len(set2_only)))
for line in list(sorted(set2_only)):
    print(line)

print(set3_onlys + ' | count: ' + str(len(set3_only)))
for line in list(sorted(set3_only)):
    print(line)

print(intersect_1_2s + ' | count: ' + str(len(intersect_1_2)))
for line in list(sorted(intersect_1_2)):
    print(line)

print(intersect_1_3s + ' | count: ' + str(len(intersect_1_3)))
for line in list(sorted(intersect_1_3)):
    print(line)

print(intersect_2_3s + ' | count: ' + str(len(intersect_2_3)))
for line in list(sorted(intersect_2_3)):
    print(line)

print(intersect_alls + ' | count: ' + str(len(intersect_all)))
for line in list(sorted(intersect_all)):
    print(line)
