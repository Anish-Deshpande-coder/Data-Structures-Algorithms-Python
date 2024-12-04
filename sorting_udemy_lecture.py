import math

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
    return array
#Time Best: O(n), Average: O(n^2) Worst: O(n^2)
#Space: O(1)

    
def selection_sort(array):
    for i in range(0, len(array)):
        smallest = i
        for j in range (i + 1, len(array)):
            if array[smallest] > array[j]:
                array[smallest], array[j] = array[j], array[smallest]
        smallest += 1
    return array
#Time Best: O(n^2), Average: O(n^2) Worst: O(n^2)
#Space: O(1)

def bubble_sort(array):
    has_swapped = False
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                has_swapped = True
        if not has_swapped:
            break
    return array
#Time Best: O(n), Average: O(n^2) Worst: O(n^2)
#Space: O(1)

def shell_sort(array):
    gaps = [5, 3, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j + gap] < array[j] and j >= 0:
                array[j], array[j + gap] = array[j + gap], array[j]
                j -= gap
    return array
#Time O(nlogn), O(n^(4/3)), O(n^(3/2)), O(nlog^(2)n), O(n^2)
#Space: O(1)

def heap_sort(array):
    heapify(array)
    for end_idx in range(len(array) - 1, 0, -1):
        array[0], array[end_idx] = array[end_idx], array[0]
        move_down(array, 0, end_idx - 1)
    return array
#Time Best: O(nlogn) Average: O(nlogn) Worst: O(nlogn)
#Space: O(1)  
    
    
def heapify(array):
    last_parent_idx = len(array) // 2 - 1
    for idx in range(last_parent_idx, -1, -1):
        move_down(array, idx, len(array) - 1)
    return array
    
def move_down(array, start_idx, end_idx):
    child_idx = 2 * start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
            start_idx = child_idx
            child_idx = 2 * start_idx + 1
        else:
            break
    
def merge_sort(array):
    if len(array) < 2:
        return array
    first_half = merge_sort(array[:len(array) // 2])
    second half = merge_sort(array[len(array) // 2:])
    return merge(first_half, second_half)
#Time O(nlogn)
#Space: O(n) 

def merge(first_half, second_half):
    result = []
    i = j = 0
    while i < len(first_half) and j < len(second_half)
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(first_half[j])
            j += 1
    while i < len(first_half):
        result.append(first_half[i])
        i += 1
    while j < len(first_half):
        result.append(second_half[j])
        j += 1
    return result

def quick_sort(array):
    if len(array) < 2:
        return array
    return partition(array, 0, len(array) - 1)
#Time Best and Average: O(nlogn) Worst: O(n^2)
#Space: O(logn) 

def partition(array, start, end):
    if start >= end:
        return
    pivot = end
    boundary = start
    for i in range(start, end):
        if array[i] <= array[pivot]:
            array[boundary], array[i] = array[i], array[boundary]
            boundary += 1
    array[boundary], array[end] = array[end], array[boundary]
    partition(array, start, boundary - 1)
    partition(array, boundary + 1, end)
    return array


def radix_sort(array):
    max_digits = get_max_number_of_digits(array)
    for i in rnage(max_digits + 1):
        buckets = [[] for _ in range(10)]
        for num in array:
            digit  = get_digit_at_position(num, position=i)
            buckets[digit].append(num)
        array = flatten(buckets)
    return array
#Time Best: O(nk) Average: O(nk) Worst: O(nk)
#Space: O(n + k)           

def get_max_number_of_digits(array):
    return max(int(math.log10(abs(num))) + 1 if num != 0 else 1 for num in array)

def get_digit_at_position(number, position):
    return (abs(number) // 10 ** position) % 10

def flatten(array):
    result = []
    for inner in array:
        for num in inner:
            result.append(num)
    return result
        
print(shell_sort([17, 59, 23, 70, 11, 42, 10, 31, 95, 20]))
print(heap_sort([95, 70, 42, 59, 20, 23, 10, 31, 17, 11]))












