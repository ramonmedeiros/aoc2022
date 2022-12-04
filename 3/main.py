#!/usr/bin/env python

with open("input", "r") as fd:
    lines = fd.read().splitlines()

def charToNumber(c):
    n = ord(c)
    if n >= 97:
        return n - 96
    return  n - 38

def convertToNumbers(string):
    l = list(string)
    i = 0
    while i < len(l):
        l[i] = charToNumber(l[i])
        i+=1
    l.sort()
    return l

def isBigger(n,biggest):
    if n is None or biggest is None:
        raise Exception()
    if n > biggest:
        return n
    return biggest

total = 0
for line in lines:
    l = len(line)
    h = int(l/2)

    first = line[0:h]
    second = line[h:]

    for c in first:
        if c in second:
            r =  charToNumber(c)
            total += r
            break

print(total)

secondTotal = 0
index = 0
while index < len(lines):

    assert lines[index] is not None
    first = convertToNumbers(lines[index])

    assert lines[index+1] is not None
    second = convertToNumbers(lines[index+1])

    assert lines[index+2] is not None
    third = convertToNumbers(lines[index+2])

    biggest = 0
    biggest = isBigger(first[0], biggest)
    biggest = isBigger(second[0], biggest)
    biggest = isBigger(third[0], biggest)

    while True:
        if first[0] == second[0] and first[0] == third[0]:
            secondTotal += first[0]
            break

        if first[0] < biggest:
            first.pop(0)
            biggest = isBigger(first[0], biggest)

        elif second[0] < biggest:
            second.pop(0)
            biggest = isBigger(second[0], biggest)

        elif third[0] < biggest:
            third.pop(0)
            biggest = isBigger(third[0], biggest)

    index+= 3

print(secondTotal)
