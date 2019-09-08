def snail(snail_map):
    if(snail_map == [[]]):
        return snail_map
    path = []
    move_state = 'right'
    traveled_x = traveled_y = 1
    pos = [0, 0]
    length_traversed = 0  
    x_moves = len(snail_map) - 1
    y_moves = len(snail_map[0]) - 1
    grid_area = len(snail_map) * len(snail_map[0])
    path.append(snail_map[pos[1]][pos[0]])
    length_traversed += 1
    while(length_traversed < grid_area):
        if(move_state is 'right'):                            
            if(x_moves == 0):
                move_state = 'down'
                traveled_x += 1
                x_moves = len(snail_map[0]) - traveled_y  
            else:
                pos[0] += 1    
                path.append(snail_map[pos[1]][pos[0]])
                x_moves -= 1
                length_traversed += 1 
        elif(move_state is 'down'):                                  
            if(y_moves == 0):
                move_state = 'left'
                traveled_y += 1
                y_moves = len(snail_map) - traveled_x 
            else:
                pos[1] += 1 
                path.append(snail_map[pos[1]][pos[0]])
                y_moves -= 1   
                length_traversed += 1  
        elif(move_state is 'left'):               
            if(x_moves == 0):
                move_state = 'up'
                traveled_x += 1
                x_moves = len(snail_map[0]) - traveled_y    
            else:
                pos[0] -= 1 
                path.append(snail_map[pos[1]][pos[0]])
                x_moves -= 1
                length_traversed += 1
        elif(move_state is 'up'):           
            if(y_moves == 0):
                move_state = 'right'
                traveled_y += 1
                y_moves = len(snail_map) - traveled_x
            else:
                pos[1] -= 1  
                path.append(snail_map[pos[1]][pos[0]])
                y_moves -= 1  
                length_traversed += 1
    return path

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# The answer that made me cry. I spent hours on the above, then I find out THIS existed. Python 2 solution.
def snail2(array):
    return list(array[0]) + snail2(zip(*array[1:])[::-1]) if array else []

print(snail(array))