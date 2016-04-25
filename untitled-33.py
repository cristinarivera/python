def proc3(n):
    if n <=3:
        return 1
    return proc3(n-1) + proc3(n-2) + proc3(n-3)

print proc3(1)
print proc3(0)
print proc3(-1)
print proc3(4)
print proc3(3)