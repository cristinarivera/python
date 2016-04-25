def find_last(s,t):    
    n = s.find(t)
    while n > 0:
        return n
        n = n + 1
    else:
        return n
        
    

print find_last('baaa','a')
#>>> 3