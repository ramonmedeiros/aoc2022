#!/usr/bin/env python

with open("input", "r") as fd:
    lines = fd.read().splitlines()

total = 0
for line in lines:
    first, second = line.split(",")

    f1,f2 = first.split('-')
    s1,s2 = second.split('-')

    f1 = int(f1)
    f2 = int(f2)
    s1 = int(s1)
    s2 = int(s2)
    
    if f1 <= s1 and s2 <= f2:
        total+=1
    elif s1 <= f1 and f2 <= s2:
        total+=1

print("workload that fully include one: " + str(total))

total = 0
for line in lines:
    first, second = line.split(",")

    f1,f2 = first.split('-')
    s1,s2 = second.split('-')

    f1 = int(f1)
    f2 = int(f2)
    s1 = int(s1)
    s2 = int(s2)
    
    if f1 > s2:
        continue
    elif s1 > f2:
        continue

    total += 1
print("workload that overlaps: " + str(total))