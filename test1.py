lost = [1,2,2,2,3,3,5]

lost.sort()

for i in range(len(lost)):
    for j in range(1, len(lost)):
        if lost[i] == lost[j]:
            lost.remove(lost[i])

print(lost)