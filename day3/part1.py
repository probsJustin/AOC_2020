with open('./puzzle','r') as fh:
    throw_away = fh.readline()
    all_lines = fh.readlines()
counterList = [3, 0]
for x in all_lines:
    if(x[counterList[0]] == "#"):
        counterList[1] = counterList[1] + 1
    counterList[0] = counterList[0] + 3
    if(counterList[0] > len(x) - 2):
        counterList[0] = counterList[0] - len(x) + 1
print(counterList[1])