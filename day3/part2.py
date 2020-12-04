def calculate_slopes(right, down):
    with open('./puzzle', 'r') as fh:
        fh.readline()
        if down == 2:
            fh.readline()
        rest_of_map = fh.readlines()
    index_dict = dict([("index", right), ("count", 0), ("cycles", 1)])
    for line in rest_of_map:
        if down == 2 and index_dict["cycles"] % 2 == 0:
            index_dict["cycles"] = index_dict["cycles"] + 1
            continue
        if line[index_dict["index"]] == "#":
            index_dict["count"] =     index_dict["count"] + 1
        index_dict["index"] = index_dict["index"] + right
        if index_dict["index"] > len(line) - 2:
            index_dict["index"] = index_dict["index"] - len(line) + 1
        index_dict["cycles"] = index_dict["cycles"] + 1
    return index_dict["count"]

print(str(calculate_slopes(1, 1)) + "," + str(calculate_slopes(3, 1)) + "," + str(calculate_slopes(5, 1)) + "," + str(calculate_slopes(7, 1)) + "," + str(calculate_slopes(1, 2)))
print(calculate_slopes(1, 1) * calculate_slopes(3, 1) * calculate_slopes(5, 1) * calculate_slopes(7, 1) * calculate_slopes(1, 2))