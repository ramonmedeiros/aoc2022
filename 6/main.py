
with open("input.txt","r") as fd:
    content = fd.read()

stringList = list(content)
#stringList= list('bvwbjplbgvbhsrlpgdmjqwftvncz')

first = 0
last = 0

def hasRepeated(t):
    for j in range(len(t)):
        for k in range(len(t)):
            if j == k:
                continue
            if t[j] == t[k]:
                return True
    return False


def foundPacket(stringList, amount):
    for i in range(len(stringList)-amount):
        
        last = i+amount
        t = stringList[i:last]
        if hasRepeated(t) is False:
            print("".join(t))
            print(last)
            break

print(foundPacket(stringList, 4))
print(foundPacket(stringList, 14))