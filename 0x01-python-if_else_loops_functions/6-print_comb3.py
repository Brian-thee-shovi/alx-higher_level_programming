#!usr/bin/python3
for ram in range(0, 10):
    for f in range(ram+1, 10):
        print("{:d}".format(f), end='')
        if ram == 8 and f == 9:
            print("{:d}".format(f), end='\n')
        else:
            print("{:d}".format(f), end=', ')
