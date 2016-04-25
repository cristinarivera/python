def proc1(input_list):
    maximum = None
    for element in input_list :
        if maximum < element:
            maximum = element
    return maximum
print proc1([30,40,50])
