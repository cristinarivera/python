value_list=[128,64,32,16,8,4,2,1]
def pattern_number(n):
    i=0    
    while True:
        p = n - value_list[i]
        if p>0:
            print value_list[i]
            p = n - value_list[i+1]
        
            
    
        
print pattern_number(125)    