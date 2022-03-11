
reader = open("input", "r")
writer = open("output", "w")

scrambled = reader.readline().strip()

count = 0
unscrambled = []
for c in scrambled:
    unscrambled.append(c)

for i in range(0, len(scrambled) - 1):
    unscrambled.sort()
    for j in range(0, len(unscrambled)):
        unscrambled[j] = scrambled[j] + unscrambled[j]

while(True):
    if (unscrambled[count][-1] == '$'):
        writer.write(unscrambled[count])
        break
    count += 1

reader.close()
writer.close()
