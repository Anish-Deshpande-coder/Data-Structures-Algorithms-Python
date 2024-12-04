def count_lowercase(s, low, high):
    if low > high:
        return 0
    count = 0
    if s[low].isupper() == False:
        count = 1
    count += count_lowercase(s, low + 1, high)
    return count

def is_number_of_lowercase_even(s, low, high):
    if low > high:
        return True
    if s[low].isupper() == False:
        return not is_number_of_lowercase_even(s, low + 1, high)
    else:
        return is_number_of_lowercase_even(s, low + 1, high)
    
