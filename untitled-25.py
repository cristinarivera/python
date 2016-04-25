def find_last(s,t):    
    ant = -1
    while True:
        end = s.find(t,ant+1)
        if end == -1:
            return ant
        ant = end    
        
        
        

print find_last('aaaa','a')
#>>> 3
print find_last('aaaaa', 'aa')
#>>> 3
print find_last('aaaa', 'b')
#>>> -1
print find_last("111111111", "1")
#>>> 8
print find_last("222222222", "")
#>>> 9
print find_last("", "3")
#>>> -1
print find_last("", "")
#>>> 0
