numbers = [1,2,3,4,5,6,7,8,9,10]

def functia(nums):
    big = nums[0]
    for num in nums:
        if num > big:
            big = num
    return big

def functia2(nums):
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
    return even

def functia3(nums):
    total_sum = 0
    for num in nums:
        if num % 3 == 0:
            total_sum += num
    return total_sum

print(functia3(numbers))