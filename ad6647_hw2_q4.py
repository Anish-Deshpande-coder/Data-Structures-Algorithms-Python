def split_parity(lst):
    odd_check = 0
    even_check = len(lst) - 1
    while even_check > odd_check:
        if lst[even_check] % 2 == 0:
            even_check -= 1
        elif lst[odd_check] % 2 != 0:
            odd_check += 1
        else:
            lst[odd_check], lst[even_check] = lst[even_check], lst[odd_check]
            odd_check += 1
            even_check -= 1
    return lst

