def split_by_sign(lst, low, high):
    if low < high:
        if lst[low] > 0 and lst[high] < 0:
            lst[low], lst[high] = lst[high], lst[low]
            split_by_sign(lst, low + 1, high - 1)
        elif lst[low] > 0:
            split_by_sign(lst, low, high - 1) 
        else:
            split_by_sign(lst, low + 1, high)