import sys

while 1:
    l = sorted(list(map(int, sys.stdin.readline().split())))
    if l == [0, 0, 0]:
        break
    print('right' if l[0]**2 + l[1]**2 == l[2]**2 else 'wrong')