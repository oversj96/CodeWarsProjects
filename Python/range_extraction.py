def solution(args):
    ranges = []
    sub_range = []
    for i in args:
        if(i+1 in args):
            sub_range.append(str(i))
        elif(len(sub_range) == 2):
            sub_range.append(str(i))
            ranges.append(str(sub_range[0]) + '-' + str(sub_range[len(sub_range)-1]))
            sub_range = [] 
        elif(len(sub_range) > 2):
            sub_range.append(str(i))
            ranges.append(str(sub_range[0]) + '-' + str(sub_range[len(sub_range)-1]))
            sub_range = []
        else:
            for x in sub_range:
                ranges.append(x)
            sub_range = []
            ranges.append(str(i))   
    return ','.join(ranges)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))