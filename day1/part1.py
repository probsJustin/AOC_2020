with open('./puzzle','r') as fh:
     all_lines = [int(i.strip()) for i in fh.readlines()]
for x in all_lines:
    for y in all_lines:
        if(x+y == 2020):
            print(x*y)
