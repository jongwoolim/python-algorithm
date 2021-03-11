s = "Ab"


count = [0] * 122
ignore_string = s.lower()

for i in range(len(s)):
    count[ord(ignore_string[i])] += 1

print(count)
answer = count.index(max(count))

print(count.index(max(count)))
print(chr(answer))

max_count = 0
for i in range(len(count)):
    if max(count) == count[i]:
        max_count += 1

print(max_count)