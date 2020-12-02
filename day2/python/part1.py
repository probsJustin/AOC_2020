with open('./puzzle', 'r') as fh:
    all_lines = fh.readlines()
valid_counter = 0
for x in all_lines:
    if(str(x.split(' ')[2].strip()).count(x.split(' ')[1][0].strip()) <= int(x.split(' ')[0].strip().split('-')[1]) and str(x.split(' ')[2].strip()).count(x.split(' ')[1][0].strip()) >= int(x.split(' ')[0].strip().split('-')[0])):
        valid_counter = valid_counter + 1
print(valid_counter)
