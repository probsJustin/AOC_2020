with open('./puzzle', 'r') as fh:
    all_lines = fh.readlines()
valid_counter =0
for x in all_lines:
    if ((x.split(' ')[2].strip()[int(x.split(' ')[0].strip().split('-')[0]) - 1] == x.split(' ')[1][0].strip()) != (x.split(' ')[2].strip()[int(x.split(' ')[0].strip().split('-')[1]) - 1] == x.split(' ')[1][0].strip())):
        valid_counter = valid_counter + 1
print(valid_counter)