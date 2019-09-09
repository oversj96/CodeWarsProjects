def move_zeros(array):
    new_array = []
    for i in array:
        if (i is not 0):
            if(type(i) is float and i != 0):
                new_array.append(i)
    for i in range(len(new_array), len(array)):
        new_array.append(0)
    return new_array

print(move_zeros([False,"a",0,0.0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))