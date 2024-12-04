def majority_number(nums):
    nums.sort() # tim sort, O(nlogn)
    return nums[len(nums)//2]


def majority_number2(nums):
    help_dict={}

    for each in nums:
        try:
            help_dict[each] += 1
        except:
            help_dict[each] = 1

    for item in help_dict.items():
        if item[1] >=len(nums)//2:
            return item[0]


def majority_number3(nums):

    candidate = None
    count = 0
    for each in nums:
        if count == 0:
            candidate = each
            count += 1
        elif candidate == each:
            count += 1
        else:
            count -= 1

    return candidate

print(majority_number([0,1,5,-1,1,1,-99,1,2,1,1]))
print(majority_number([0,1,5,-1,1,99,99,99,99,99,99]))
