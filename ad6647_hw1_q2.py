def shift(lst, k, direction='left'):
    list_length = len(lst)
    k %= list_length
    if direction == 'left':
        lst[:] = lst[k:] + lst[:k]
    elif direction == 'right':
        lst[:] = lst[-k:] + lst[:-k]
    else:
        raise Exception("enter 'left' or 'right' for direction")
            
            
    
    