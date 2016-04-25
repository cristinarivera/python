spy = [0,0,7]
p = spy
def replace_spy(p):
    p[2] = p[2]+1


replace_spy(spy)
print spy
#>>> [0,0,8]