#!/usr/bin/python3
"""
mods documentation that reads standard input and
computes metrics
"""


from sys import stdin


status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

total_size = i = 0


def print_status():
    """func computes metrics"""
    print(f'File size: {totalsize_t}')
    for ky, v_value in sorted(status_codes.items()):
        if v_value > 0:
            print('{:s}: {:d}'.format(ky, v_value))


try:
    for line in stdin:
        spt_line = line.split()
        if len(spt_line) >= 2:
            status = spt_line[-2]
            total_size += int(spt_line[-1])
            if status in status_codes:
                status_codes[status] += 1

        w = w + 1

        if w % 10 == 0:
            print_status()
    print_status()
except KeyboardInterrupt as e:
    print_status()
