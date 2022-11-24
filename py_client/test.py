from copy import copy


nums = [1,2,3,4]


new = copy(nums)
print(new)
def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num += num
    # print(max_num)