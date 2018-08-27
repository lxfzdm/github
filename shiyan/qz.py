import sys
for i in sorted(list(map(lambda c:c.strip(),sys.stdin.readlines()[1:])),key=lambda c:c):
    print(i)