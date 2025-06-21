def riverSizes(matrix):

    mtx = matrix

    len_y = len(mtx) - 1
    len_x = len(mtx[0]) - 1

    explored = {} # areas already explored
    river_lengths = []

    def mk_direction_dict(idx_y, idx_x):

        if 'above':
            if idx_y - 1 < 0:
                above = 'oob'
            else:
                above = {
                     'val':         mtx[idx_y - 1][idx_x]
                    ,'str_idx':     f'{idx_y - 1}, {idx_x}'
                    ,'is_explored': explored.get(f'{idx_y - 1}, {idx_x}')
                    }
        if 'below':
            if idx_y + 1 > len_x:
                below = 'oob'
            else:
                below = {
                     'val':         mtx[idx_y + 1][idx_x]
                    ,'str_idx':     f'{idx_y + 1}, {idx_x}'
                    ,'is_explored': explored.get(f'{idx_y + 1}, {idx_x}')
                    }
        if 'right':
            if idx_x + 1 > len_x:
                right = 'oob'
            else:
                right = {
                     'val':         mtx[idx_y][idx_x + 1]
                    ,'str_idx':     f'{idx_y}, {idx_x + 1}'
                    ,'is_explored': explored.get(f'{idx_y}, {idx_x + 1}')        
                    }
        if 'left':
            if idx_x - 1 < 0:
                left = 'oob'
            else:
                left = {
                     'val':         mtx[idx_y][idx_x - 1]
                    ,'str_idx':     f'{idx_y}, {idx_x - 1}'
                    ,'is_explored': explored.get(f'{idx_y}, {idx_x - 1}')
                    }
        else:
            return None
        
        return above, below, right, left
    
    def check_direction(direction_dict):
        direction = direction_dict
        if direction != 'oob':
            if not direction['is_explored'] and direction['val']:
                return True
        return False
    
    def more_river(direction_dict, idx_y, idx_x, river_length):
        explored[direction_dict['str_idx']] = True
        river_length.append(1)
        continue_down_this_river(idx_y - 1, idx_x, river_length)

    def continue_down_this_river(idx_y, idx_x, river_length):
        above, below, right, left = mk_direction_dict(idx_y, idx_x)

        # if there's more river...
        # above
        if check_direction(above):
            more_river(above, idx_y - 1, idx_x, river_length)
        # below
        elif check_direction(below):
            more_river(below, idx_y + 1, idx_x, river_length)
        # right
        elif check_direction(right):
            more_river(right, idx_y, idx_x + 1, river_length)
        # left
        elif check_direction(left):
            more_river(left, idx_y, idx_x - 1, river_length)
        # if there's no more river
        river_length = sum(river_length)
        return river_length

    for idx_y, row in enumerate(mtx):
        for idx_x, xy in enumerate(row):
            if not explored.get(f'{idx_y}, {idx_x}'):
                explored[f'{idx_y}, {idx_x}'] = True
                if xy: # if it's a river, continue down it
                    river_length = [1]
                    river_lengths.append(continue_down_this_river(idx_y, idx_x, river_length))
    
    return river_lengths