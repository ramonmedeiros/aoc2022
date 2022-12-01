#!/usr/bin/env python


with open("input","r") as fd:
    lines = fd.read().splitlines()

elves = []
lastElve = 0
index = 0
total = 0
while index < len(lines):
    if lines[index] == "":
        elves.append(total)
        total = 0
        lastElve = index - 1
    else:
        total += int(lines[index])
    index+=1

elves.sort()
print("elve with most calories " + str(elves[-1]))
print("top 3 elves with sum calories " + str(elves[-1]+elves[-2]+elves[-3]))
