def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        if lst01[mid] == 0 and lst01[mid + 1] == 1:
            return (mid + 1)
        if lst01[mid] == 1 and lst01[mid - 1] == 0:
            return mid
        elif lst01[mid] == 1:
            right = mid - 1
        elif lst01[mid] == 0:
            left = mid + 1


                
                
            
    