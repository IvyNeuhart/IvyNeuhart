import re
hand = open("regex_sum_1888114.txt")
numlist = list()
#sum = 0
for line in hand:
    line = line.rstrip()
    dataPoints = re.findall('[0-9]+', line)
    if len(dataPoints) < 1: continue
    #print(dataPoints)
    for i in range(len(dataPoints)):
        num = int(dataPoints[i])
        numlist.append(num)
        #sum = sum + num

#print(numlist)
print(sum(numlist))
